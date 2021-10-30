#!/bin/bash

set -x
curl -X GET -c cookie.txt http://localhost:8000/login/ | grep csrfmiddlewaretoken
curl -i -X POST -b cookie.txt -c cookie.txt -d 'mail=fuga@test.hoge.jp&password=password&csrfmiddlewaretoken=XXXXX' http://localhost:8000/login
curl -X POST -b cookie.txt -d 'isbn=9784839975869' http://localhost:8000/book
curl -X POST -b cookie.txt -d 'isbn=9784873113593' http://localhost:8000/book
# Existing ISBN
curl -X GET -b cookie.txt http://localhost:8000/search?isbn=9784839975869
curl -X GET -b cookie.txt http://localhost:8000/search?isbn=9784873113593
set +x
