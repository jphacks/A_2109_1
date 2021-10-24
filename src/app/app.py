from flask import Flask, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import pymysql

from app import top

app = Flask(__name__)
app.secret_key = 'please change later'
app.register_blueprint(top.bp)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id


db = pymysql.connect(
    host="db",
    user='root',
    password='rootpw',
    db='main',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
    )

@login_manager.user_loader
def user_loader(uid):
    user = User(uid)
    return user

@app.route('/login', methods=['POST'])
def login():
    mail = request.form["mailAddress"]
    password = request.form["password"]
    with db.cursor() as cursor:
        sql = "SELECT ID from user where mailAddress = %s and password = %s" 
        cursor.execute(sql, (mail, password))
        result = cursor.fetchall()
        print(type(result))
        print(result)
        if len(result) == 0:
            print("Error")
            return
        else:
            login_user(User(result[0]['ID']))
            print("Redirect")
            return "Successfully Logined!"


@app.route('/logout')
def logout():
    logout_user()
    return 'Log Out'


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'


@app.route("/")
def hello():
    with db.cursor() as cursor:
        sql = "SELECT name FROM user;"
        cursor.execute(sql)
        result = cursor.fetchall()

        return ','.join([name["name"] for name in result])


if __name__ == "__main__":
    app.run(debug=True)
