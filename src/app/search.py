from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app import app

bp = Blueprint('search', __name__)

@bp.route('/search', methods=['GET'])
@login_required
def search():
    with app.db.cursor() as cursor:
        isbn = request.args['isbn']
        sql = '''
        SELECT * FROM book
        where isbn = %s;
        '''
        cursor.execute(sql, isbn)
        result = cursor.fetchall()
        print(result)
        if len(result) == 0:
            #　検索結果なし(本、未登録)の場合
            return jsonify({'message': 'Error: The target book is not registered.'}), 404

        sql = '''
        SELECT * FROM user_pinned
        WHERE userID = %s and bookID = %s
        '''
        cursor.execute(sql, (current_user.id, result[0]['ID']))
        isPinned = bool(len(cursor.fetchall()) != 0)
        
        #　検索結果あり(本,登録済み)の場合
        return jsonify(
            {'ID': result[0]['ID'],
                'title': result[0]['title'],
                'isbn': result[0]['isbn'],
                'author': result[0]['author'],
                'publishDate': result[0]['publishDate'],
                'amazonLink': result[0]['amazonLink'],
                'isPinned': isPinned}), 200