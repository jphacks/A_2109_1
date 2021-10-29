from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app import app
import pymysql

bp = Blueprint('article', __name__, url_prefix='/article')

@bp.route('', methods=['GET'])
@login_required
def getArticles():
    bookID = request.args['bookID']

    with app.db.cursor() as cursor:
        sql = '''
        SELECT article.ID, article.userID, context, updatedDate, chapter, page,
        COUNT(user_likes.ID) as likeNum
        FROM article
        LEFT JOIN user_likes
        ON article.ID = user_likes.articleID
        where article.bookID = %s
        GROUP BY article.ID
        '''

        cursor.execute(sql, bookID)
        result = cursor.fetchall()
        print(result)
        return jsonify({"articles": result}), 400


@bp.route('', methods=['DELETE'])
@login_required
def deleteArticle():
    articleID = request.args['articleID']
    # 存在確認
    with app.db.cursor() as cursor:
        sql = '''
        DELETE article, book_marks, user_likes FROM article
        LEFT JOIN book_marks
        ON article.ID = book_marks.articleID
        LEFT JOIN user_likes
        ON article.ID = user_likes.articleID
        WHERE article.ID = %s
        '''
        try:
            cursor.execute(sql, articleID)
            app.db.commit()
        except pymysql.Error as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            return {"message": e.args[1]}, 400

        return jsonify({"message": "Successfully deleted"}), 200


@bp.route('', methods=['PUT'])
@login_required
def updateArticle():
    articleID = request.args['articleID']
    context = request.args['context']


@bp.route('/like', methods=['POST'])
@login_required
def registerLike():
    articleID = request.args['articleID']
    userID = current_user.id
    with app.db.cursor() as cursor:
        # 登録済みかチェック
        sql = '''
        SELECT COUNT(ID) FROM user_likes
        WHERE articleID = %s AND userID = %s
        '''
        cursor.execute(sql, (userID, articleID))
        if(cursor.fetchall() != 0):
            return jsonify({"message": "Already Liked"}), 409

        # 登録
        sql = 'INSERT INTO user_likes VALUES(0, %s, %s)'
        cursor.execute(sql, (0, userID, articleID))
        app.db.commit()
        return jsonify({"message": "Successfully Registerd"}), 201


@bp.route('/bookmark', methods=['POST'])
@login_required
def registerBookmark():
    articleID = request.args['ID']
    userID = current_user.id
    with app.db.cursor() as cursor:
        # 登録済みかチェック
        sql = '''
        SELECT COUNT(ID) FROM book_marks 
        WHERE articleID = %s AND userID = %s
        '''
        cursor.execute(sql, (userID, articleID))
        if(cursor.fetchall() != 0):
            return jsonify({"message": "Already Marked"}), 409

        # 登録
        sql = 'INSERT INTO book_marks VALUES(0, %s, %s)'
        cursor.execute(sql, (0, userID, articleID))
        app.db.commit()
        return jsonify({"message": "Successfully Registerd"}), 201