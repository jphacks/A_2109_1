from flask import Blueprint, request, jsonify
from flask_login import login_required
from app import app

bp = Blueprint('book', __name__)

@bp.route('/book', methods=['POST'])
@login_required
def book():
    title = request.form['title']
    isbn = request.form['isbn']
    author = request.form['author']
    publishDate = request.form['publishDate']
    amazonLink = request.form.get('amazonLink')
    with app.db.cursor() as cursor:
        sql = '''
        INSERT INTO book VALUES
        (0, %s, %s, %s, %s, %s)
        '''
        cursor.execute(sql, (title, isbn, author, publishDate, amazonLink))

        app.db.commit()
        return jsonify({"message": "Succcessfully registered"}), 400