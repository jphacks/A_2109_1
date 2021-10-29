from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app import app

bp = Blueprint('top', __name__)

@bp.route('/top', methods=['GET'])
@login_required
def top():
    with app.db.cursor() as cursor:
        #sql ='''
        #SELECT book.ID
        #FROM book
        #GROUP BY book.ID DESC 
        #LIMIT 0,10
        #'''
        #cursor.execute(sql)
        #result = cursor.fetchall()
        
        print(result)
        return jsonify({"message": "Successfully!!", "articles": result}), 400