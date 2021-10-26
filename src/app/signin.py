from flask import Blueprint, request, jsonify
from flask_login import login_user
from app import app

bp = Blueprint('signin', __name__)

@bp.route('/signin', methods=["post"])
def signin():
    user_name = request.form["user_name"]
    mailAddress = request.form["mailAddress"]
    password = request.form["password"]
    user_image = request.form["user_image"]

    with app.db.cursor() as cursor:
        sql = "SELECT ID from user where mailAddress = %s"
        cursor.execute(sql, (mailAddress))
        # メールアドレスが既に登録されていないか確認
        result = cursor.fetchall()
        print(result)
        if len(result) != 0:
            return jsonify({'message': 'Error: Already registered mail address.'}), 409
        else:
            # ユーザー登録
            sql = "INSERT INTO user VALUES(0, %s, %s, %s, %s)"
            cursor.execute(sql, (user_name, password, mailAddress, user_image))
            app.db.commit()
            # ログイン
            sql = "SELECT ID from user where mailAddress = %s"
            cursor.execute(sql, (mailAddress))
            result =  cursor.fetchall()
            login_user(app.User(result[0]['ID']))

            return jsonify({'message': 'Successfully registered.'}), 201
