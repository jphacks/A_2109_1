from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app import app
import pymysql
import datetime

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
        return jsonify({"message": "Successfully!!", "articles": result}), 400


def isArticleExisit(articleID):
    with app.db.cursor() as cursor:
        sql = 'SELECT ID FROM article WHERE ID = %s'
        cursor.execute(sql, articleID)
        result = cursor.fetchall()
        return len(result) != 0


@bp.route('', methods=['POST'])
@login_required
def putArticles(): 
    bookID = request.form['bookID']
    context = request.form['context']
    chapter = request.form.get('chapter')
    page = request.form.get('page')

    with app.db.cursor() as cursor:
        sql = '''
        INSERT INTO article VALUES
        (0, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(sql, (current_user.id, bookID, context, 
            datetime.date.today(), chapter, page))

        app.db.commit()
        return jsonify({"message": "Succcessfully registered"}), 400


@bp.route('', methods=['DELETE'])
@login_required
def deleteArticle():
    articleID = request.args['articleID']
    if(not isArticleExisit(articleID)):
        return jsonify({"message": "The article is not found"}), 404

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
    articleID = request.form['articleID']

    if(not isArticleExisit(articleID)):
        return jsonify({"message": "The article is not found"}), 404

    with app.db.cursor() as cursor:
        param = dict(filter(lambda i: i[1] != None and i[0] != 'articleID', request.form.items()))

        sets = map(lambda x: x + ' = %s', param.keys())
        sql = 'UPDATE article set '
        sql += ','.join(sets)
        sql += 'WHERE ID = %s'

        cursor.execute(sql, list(param.values()) + [articleID])
        app.db.commit()
        
    return jsonify({"message": "Successfully update"}), 200


@bp.route('/like', methods=['POST'])
@login_required
def registerLike():
    articleID = request.form['articleID']
    userID = current_user.id
    if(not isArticleExisit(articleID)):
        return jsonify({"message": "The article is not found"}), 404

    with app.db.cursor() as cursor:
        # 登録済みかチェック
        sql = '''
        SELECT COUNT(ID) FROM user_likes
        WHERE userID = %s AND articleID = %s
        '''
        cursor.execute(sql, (userID, articleID))
        if(cursor.fetchone()['COUNT(ID)'] != 0):
            return jsonify({"message": "Already Liked"}), 409

        # 登録
        sql = 'INSERT INTO user_likes VALUES(0, %s, %s)'
        cursor.execute(sql, (userID, articleID))
        app.db.commit()
        return jsonify({"message": "Successfully Registerd"}), 201


@bp.route('/bookmark', methods=['POST'])
@login_required
def registerBookmark():
    articleID = request.form['articleID']
    userID = current_user.id
    if(not isArticleExisit(articleID)):
        return jsonify({"message": "The article is not found"}), 404

    with app.db.cursor() as cursor:
        # 登録済みかチェック
        sql = '''
        SELECT COUNT(ID) FROM book_marks 
        WHERE userID = %s AND articleID = %s
        '''
        cursor.execute(sql, (userID, articleID))
        if(cursor.fetchone()['COUNT(ID)'] != 0):
            return jsonify({"message": "Already Marked"}), 409

        # 登録
        sql = 'INSERT INTO book_marks VALUES(0, %s, %s)'
        cursor.execute(sql, (userID, articleID))
        app.db.commit()
        return jsonify({"message": "Successfully Registerd"}), 201