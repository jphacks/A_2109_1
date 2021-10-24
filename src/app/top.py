from flask import Blueprint
from flask_login import login_required, current_user
from app import app

bp = Blueprint('top', __name__)

@bp.route('/top')
@login_required
def top():
    with app.db.cursor() as cursor:
        sql = "SELECT name FROM user where ID = %s;"
        cursor.execute(sql, current_user.id)
        result = cursor.fetchall()

        return 'User Name is ' + result[0]['name']