from flask import Flask
import pymysql

app = Flask(__name__)

@app.route("/")
def hello():

    db = pymysql.connect(
        host="db",
        user='root',
        password='rootpw',
        db='main',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
        )

    with db.cursor() as cursor:
        sql = "SELECT name FROM user;"
        cursor.execute(sql)
        result = cursor.fetchall()

        return ','.join([name["name"] for name in result])


if __name__ == "__main__":
    app.run(debug=True)
