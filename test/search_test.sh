#!/bin/bash

set -x
curl -X GET -c cookie.txt http://localhost:8000/login/ | grep csrfmiddlewaretoken
curl -i -X POST -b cookie.txt -c cookie.txt -d 'mail=fuga@test.hoge.jp&password=password&csrfmiddlewaretoken=XXXXX' http://localhost:8000/login
# Existing ISBN
curl -X GET -b cookie.txt http://localhost:8000/search?isbn=9784627705623 
# Not existing ISBN
curl -X GET -b cookie.txt -d http://localhost:8000/search?isbn=8784627705623
set +x
