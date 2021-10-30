from flask import Blueprint, request, jsonify
from flask_login import login_user
from app import app

bp = Blueprint('signin', __name__)

@bp.route('/signin', methods=["post"])
def signin():
    name = request.form["name"]
    mail = request.form["mail"]
    password = request.form["password"]
    image = request.form.get("image")

    with app.db.cursor() as cursor:
        sql = "SELECT ID from user where mailAddress = %s"
        cursor.execute(sql, (mail))
        # メールアドレスが既に登録されていないか確認
        result = cursor.fetchall()
        print(result)
        if len(result) != 0:
            return jsonify({'message': 'Error: Already registered mail address.'}), 409
        else:
            # ユーザー登録
            sql = "INSERT INTO user VALUES(0, %s, %s, %s, %s)"
            cursor.execute(sql, (name, password, mail, image))
            app.db.commit()
            # ログイン
            sql = "SELECT ID from user where mailAddress = %s"
            cursor.execute(sql, (mail))
            result =  cursor.fetchall()
            login_user(app.User(result[0]['ID']))

            return jsonify({'message': 'Successfully registered.'}), 201
