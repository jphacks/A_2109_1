from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app import app

bp = Blueprint('user', __name__)

@bp.route('/user', methods=['GET'])
@login_required
def user():
    with app.db.cursor() as cursor:
        sql = '''
        SELECT name, image
        FROM user
        WHERE ID = %s
        '''
        cursor.execute(sql, current_user.id)
        result = cursor.fetchall()[0]

        # いいね一覧
        sql = '''
        SELECT article.ID, article.userID, article.bookID, context, updatedDate, chapter, page,
        COUNT(user_likes.ID) as likeNum
        FROM article
        LEFT JOIN user_likes
        ON article.ID = user_likes.articleID
        where user_likes.userID = %s 
        GROUP BY article.ID
        '''
        cursor.execute(sql, current_user.id)
        result['likes'] = cursor.fetchall()

        # ブックマーク一覧
        sql = '''
        SELECT article.ID, article.userID, article.bookID, context, updatedDate, chapter, page,
        COUNT(user_likes.ID) as likeNum
        FROM article
        LEFT JOIN user_likes
        ON article.ID = user_likes.articleID
        LEFT JOIN book_marks
        ON article.ID = book_marks.articleID
        where book_marks.userID = %s 
        GROUP BY article.ID
        '''
        cursor.execute(sql, current_user.id)
        result['bookmarks'] = cursor.fetchall()

        # 投稿記事一覧
        sql = '''
        SELECT article.ID, article.userID, article.bookID, context, updatedDate, chapter, page,
        COUNT(user_likes.ID) as likeNum
        FROM article
        LEFT JOIN user_likes
        ON article.ID = user_likes.articleID
        where article.userID = %s 
        GROUP BY article.ID
        '''
        cursor.execute(sql, current_user.id)
        result['posted'] = cursor.fetchall()

        print(result)

        return jsonify({"message": "Succcessfully registered"}), 400