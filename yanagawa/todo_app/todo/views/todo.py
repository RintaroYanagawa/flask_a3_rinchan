from flask import request, redirect, url_for, render_template, flash, jsonify, session
from todo import app, db
from todo.models.users import Users, Todos
import requests


@app.route("/api/todos/<string:user_id>", methods=["GET"])
def select_todos(user_id):
    todos = list(
        map(
            lambda todo: {
                "id": todo.id,
                "public_id": todo.public_id,
                "title": todo.title,
                "contents": todo.contents,
                "limit": todo.limit,
                "is_done": todo.is_done,
                "user_id": todo.user_id,
                "created_at": todo.created_at,
                "updated_at": todo.updated_at,
            },
            Todos.query.filter_by(user_id=user_id).all(),
        )
    )

    return jsonify({"ok": True, "data": todos})


@app.route("/api/todo/<string:id>", methods=["GET"])
def select_todo(id):
    todo = Todos.query.filter_by(public_id=id).first()

    if todo is None:
        return jsonify({"ok": False, "error": "not exists todo"})

    uuid = todo.id
    public_id = todo.public_id
    title = todo.title
    contents = todo.contents
    limit = todo.limit
    is_done = todo.is_done
    user_id = todo.user_id
    created_at = todo.created_at
    updated_at = todo.updated_at

    return jsonify(
        {
            "ok": True,
            "data": [
                {
                    "uuid": uuid,
                    "public_id": public_id,
                    "title": title,
                    "contents": contents,
                    "limit": limit,
                    "is_done": is_done,
                    "user_id": user_id,
                    "created_at": created_at,
                    "updated_at": updated_at,
                }
            ],
        }
    )


@app.route("/api/todo", methods=["POST"])
def create_todo():
    json = request.get_json()

    title = json["title"]
    contents = json["contents"]
    limit = json["limit"]
    user_id = json["user_id"]

    todo = Todos(title=title, contents=contents, limit=limit, user_id=user_id)

    db.session.add(todo)
    db.session.commit()

    return jsonify(
        {
            "ok": True,
            "data": {
                "title": title,
                "contents": contents,
                "limit": limit,
                "user_id": user_id,
            },
        }
    )


@app.route("/api/todo", methods=["PATCH"])
def update_todo():
    json = request.get_json()

    public_id = json["public_id"]
    title = json["title"]
    contents = json["contents"]
    limit = json["limit"]
    is_done = json["is_done"]
    user_id = json["user_id"]

    todo = db.session.query(Todos).filter_by(public_id=public_id).first()
    todo.title = title
    todo.contents = contents
    todo.is_done = is_done

    db.session.commit()

    return jsonify(
        {
            "ok": True,
            "data": {
                "public_id": public_id,
                "title": title,
                "contents": contents,
                "limit": limit,
                "is_done": is_done,
                "user_id": user_id,
            },
        }
    )


@app.route("/list", methods=["GET"])
def show_list():
    user_id = session.get("logged_userid")
    response = requests.get(f"http://127.0.0.1:5000/api/todos/{user_id}")

    json = response.json()

    todos = json["data"]

    return render_template("list.html", todos=todos)


@app.route("/todo/new", methods=["GET"])
def show_todo_new():
    return render_template("new.html")


@app.route("/todo/new", methods=["POST"])
def todo_new():
    user_id = session.get("logged_userid")
    title = request.form["title"]
    contents = request.form["contents"]
    limit = request.form["limit"]

    response = requests.post(
        "http://127.0.0.1:5000/api/todo",
        json={"title": title, "contents": contents, "limit": limit, "user_id": user_id},
    )

    json = response.json()
    print(json)

    return redirect(url_for("show_list"))


@app.route("/todo/<string:public_id>", methods=["GET"])
def show_todo(public_id):
    response = requests.get(
        f"http://127.0.0.1:5000/api/todo/{public_id}",
    )

    json = response.json()

    return render_template("todo.html", todo=json["data"][0])
