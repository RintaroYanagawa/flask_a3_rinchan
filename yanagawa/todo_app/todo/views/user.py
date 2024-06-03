from flask import request, redirect, url_for, render_template, flash, jsonify
from todo import app, db
from todo.models.users import Users


@app.route("/api/users", methods=["GET"])
def select_users():
    users = list(
        map(
            lambda user: {
                "id": user.id,
                "public_id": user.public_id,
                "name": user.name,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
            },
            Users.query.all(),
        )
    )

    return jsonify({"ok": True, "data": users})


@app.route("/api/user", methods=["POST"])
def create_user():
    json = request.get_json()

    print(json)

    public_id = json["public_id"]
    password = json["password"]
    name = json["name"]

    exists_user = Users.query.filter_by(public_id=public_id).first() is not None
    if exists_user:
        return jsonify({"ok": False, "error": "already exists user"})

    user = Users(public_id=public_id, password=password, name=name)
    db.session.add(user)
    db.session.commit()

    return jsonify(
        {
            "ok": True,
            "data": {"public_id": public_id, "password": password, "name": name},
        }
    )


@app.route("/api/user/<string:id>", methods=["GET"])
def select_user(id):
    user = Users.query.get(id)
    if user is None:
        return jsonify({"ok": False, "error": "not exists user"})

    uuid = user.id
    public_id = user.public_id
    name = user.name
    created_at = user.created_at
    updated_at = user.updated_at

    return jsonify(
        {
            "ok": True,
            "data": [
                {
                    "id": uuid,
                    "public_id": public_id,
                    "name": name,
                    "created_at": created_at,
                    "updated_at": updated_at,
                }
            ],
        }
    )
