from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app import app
import pymysql

bp = Blueprint('top', __name__)

@bp.route('/top', methods=['GET'])
@login_required
def top():
    with app.db.cursor() as cursor:
        # おすすめ
        sql ='''
        SELECT *
        FROM book 
        order by ID desc
        limit 10
        '''
        cursor.execute(sql)
        recommendBook = cursor.fetchall()

        # ピン留め
        sql ='''
        SELECT * FROM book
        INNER JOIN (
            SELECT * FROM user_pinned
            WHERE user_pinned.userID = %s
        ) AS pin
        ON book.ID = pin.bookID
        '''

        cursor.execute(sql, current_user.id)
        pinnedBook = cursor.fetchall()
        print(resultA)
        print(resultB)
        return jsonify({"message": "Successfully!!", "recommendBook": recommendBook, "pinnedBook" : pinnedBook}), 200