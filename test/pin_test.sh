#!/bin/bash

set -x
curl -X GET -c cookie.txt http://localhost:8000/login/ | grep csrfmiddlewaretoken
curl -i -X POST -b cookie.txt -c cookie.txt -d 'mail=fuga@test.hoge.jp&password=password&csrfmiddlewaretoken=XXXXX' http://localhost:8000/login
curl -X POST -b cookie.txt -d 'bookID=1' http://localhost:8000/article/pin
set +x
