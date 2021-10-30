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
        #sql ='''
        #SELECT *
        #FROM book 
        #order by ID desc
        #limit 10
        #'''
        #cursor.execute(sql)
        #resultA = cursor.fetchall()

        # ピン留め
        sql ='''
        SELECT *
        LEFT JOIN user_pinned
        ON book.ID = user_pinned.bookID
        FROM book
        where user_pinnned.userID = %s
        '''

        cursor.execute(sql, current_user.id)
        resultB = cursor.fetchall()
        #print(resultA)
        print(resultB)
        return jsonify({"message": "Successfully!!", "booksB": resultB}), 400