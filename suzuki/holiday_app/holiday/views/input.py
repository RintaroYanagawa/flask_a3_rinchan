from flask import request, redirect, url_for, render_template, flash, session
from holiday import app, db
from holiday.models.mst_holiday import Holiday
# from holiday.views.views import login_required


@app.route("/", methods=["GET", "POST"])
def input():
    input_data = session.get("input_data", None)
    return render_template("input.html", input_data=input_data)





# @app.route('/entries/new', methods=['GET'])
# @login_required
# def new_entry():
#     return render_template('entries/new.html')


# @app.route('/entries/<int:id>', methods=['GET'])
# @login_required
# def show_entry(id):
#     entry = Entry.query.get(id)
#     return render_template('entries/show.html', entry=entry)


# @app.route('/entries/<int:id>/edit',methods=['GET'])
# @login_required
# def edit_entry(id):
#     entry = Entry.query.get(id)
#     return render_template('entries/edit.html',entry=entry)


# @app.route('/entries/<int:id>/update', methods=['POST'])
# @login_required
# def update_entry(id):
#     entry = Entry.query.get(id)
#     entry.title = request.form['title']
#     entry.text = request.form['text']
#     db.session.merge(entry)
#     db.session.commit()
#     flash('記事が更新されました')
#     return redirect(url_for('show_entries'))


# @app.route('/entries/<int:id>/delete', methods=['POST'])
# @login_required
# def delete_entry(id):
#     entry = Entry.query.get(id)
#     db.session.delete(entry)
#     db.session.commit()
#     flash('投稿が削除されました')
#     return redirect(url_for('show_entries'))
