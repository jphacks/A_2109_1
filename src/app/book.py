from flask import Blueprint, request, jsonify
from flask_login import login_required
from app import app
import urllib, json

bp = Blueprint('book', __name__)

def getData(isbn):
    url = 'http://api.openbd.jp/v1/get?isbn=' + isbn
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        return json.load(res)

def convertISBN(isbn13):
    isbn10 = isbn13[3:12]
    check_digit = 0
    for i in range(len(isbn10)):
        check_digit += int(isbn10[i]) * (10 - i)

    check_digit = 11 - (check_digit % 11)

    if check_digit == 10:
        check_digit = 'X'
    elif check_digit == 11:
        check_digit = '0'
    else:
        check_digit = str(check_digit)

    isbn10 += check_digit
    return 'http://www.amazon.co.jp/dp/' + isbn10 + '/'


@bp.route('/book', methods=['POST'])
@login_required
def book():
    isbn = request.form['isbn']
    body = getData(isbn)[0]['onix']
    title = body['DescriptiveDetail']['TitleDetail']['TitleElement']['TitleText']['content']
    authors = '\n'.join([author['PersonName']['content'] for author in body['DescriptiveDetail']['Contributor']])
    imageLink = body['CollateralDetail']['SupportingResource'][0]['ResourceVersion'][0]['ResourceLink']
    amazonLink = convertISBN(isbn)
    
    print(title, authors, imageLink, amazonLink)
    
    with app.db.cursor() as cursor:
        sql = '''
        INSERT INTO book VALUES
        (0, %s, %s, %s, %s, %s)
        '''
        cursor.execute(sql, (title, isbn, authors, imageLink, amazonLink))

        app.db.commit()
        return jsonify({"message": "Succcessfully registered"}), 400