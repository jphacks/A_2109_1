#!/bin/bash

set -x
curl -X GET -c cookie.txt http://localhost:8000/login/ | grep csrfmiddlewaretoken
curl -i -X POST -b cookie.txt -c cookie.txt -d 'mailAddress=fuga@test.hoge.jp&password=password&csrfmiddlewaretoken=XXXXX' http://localhost:8000/login

curl -X GET -b cookie.txt http://localhost:8000/article?bookID=1
curl -X DELETE -b cookie.txt http://localhost:8000/article?articleID=1
curl -X GET -b cookie.txt http://localhost:8000/article?bookID=1
curl -X DELETE -b cookie.txt http://localhost:8000/article?articleID=100
set +x
