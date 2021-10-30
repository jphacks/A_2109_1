#!/bin/bash

set -x
curl -X GET -c cookie.txt http://localhost:8000/login/ | grep csrfmiddlewaretoken
curl -i -X POST -b cookie.txt -c cookie.txt -d 'mailAddress=fuga@test.hoge.jp&password=password&csrfmiddlewaretoken=XXXXX' http://localhost:8000/login
curl -X POST -b cookie.txt -d 'title=KozimaDaikiNoZinsei&isbn=1234567891234&author=KozimaDaiki&publishDate=2000-01-04&amazonLink=localhost:8000' http://localhost:8000/book
curl -X POST -b cookie.txt -d 'title=TachiYoshikiNoZinsei&isbn=1234567891230&author=TachiYoshiki&publishDate=1999-07-16' http://localhost:8000/book
# Existing ISBN
curl -X GET -b cookie.txt http://localhost:8000/search?isbn=1234567891234
curl -X GET -b cookie.txt http://localhost:8000/search?isbn=1234567891230
set +x