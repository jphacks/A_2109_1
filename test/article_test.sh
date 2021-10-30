#!/bin/bash

set -x
curl -X GET -c cookie.txt http://localhost:8000/login/ | grep csrfmiddlewaretoken
curl -i -X POST -b cookie.txt -c cookie.txt -d 'mail=fuga@test.hoge.jp&password=password&csrfmiddlewaretoken=XXXXX' http://localhost:8000/login

curl -X GET -b cookie.txt http://localhost:8000/article?bookID=5
curl -X GET -b cookie.txt http://localhost:8000/article?bookID=2

curl -X DELETE -b cookie.txt http://localhost:8000/article?articleID=1
curl -X GET -b cookie.txt http://localhost:8000/article?bookID=1
curl -X DELETE -b cookie.txt http://localhost:8000/article?articleID=100

curl -X POST -b cookie.txt -d 'bookID=1&context=test&chapter=10&page=100' http://localhost:8000/article
curl -X POST -b cookie.txt -d 'bookID=1&context=test&chapter=1' http://localhost:8000/article
curl -X GET -b cookie.txt http://localhost:8000/article?bookID=1

curl -X PUT -b cookie.txt -d 'articleID=7&context=hogehoge&chapter=1' http://localhost:8000/article
curl -X PUT -b cookie.txt -d 'articleID=8&context=fugafuga&' http://localhost:8000/article
curl -X GET -b cookie.txt http://localhost:8000/article?bookID=1

# Like
curl -X POST -b cookie.txt -d 'articleID=7' http://localhost:8000/article/like
curl -X POST -b cookie.txt -d 'articleID=7' http://localhost:8000/article/like

# Bookmark
curl -X POST -b cookie.txt -d 'articleID=7' http://localhost:8000/article/bookmark
curl -X POST -b cookie.txt -d 'articleID=7' http://localhost:8000/article/bookmark

set +x
