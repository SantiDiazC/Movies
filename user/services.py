from flask import request, render_template

from Movies import app
from user.models import User


@app.route('/save-user', methods=["POST"])
def save_user():
    data = request.form
    name = data.get("name", None)
    nickname = data.get("nickname", None)
    password = data.get("password", None)
    if name and nickname and password:
        User(
            name=name,
            nickname=nickname,
            password=password
        ).save()

    return render_template("test.html")