from flask import Blueprint, request, jsonify
from flask_login import login_required
from app import app

bp = Blueprint('user', __name__)

@bp.route('/user', methods=['GET'])
@login_required
def book():
    with app.db.cursor() as cursor:
        sql = '''
        SELECT name, image
        FROM user
        WHERE ID = %s
        '''

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

        cursor.execute(sql)
        cursor.fetchall()
        return jsonify({"message": "Succcessfully registered"}), 400