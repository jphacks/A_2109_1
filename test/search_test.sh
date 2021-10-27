#!/bin/bash

set -x
curl -X GET -c cookie.txt http://localhost:8000/login/ | grep csrfmiddlewaretoken
curl -i -X POST -b cookie.txt -c cookie.txt -d 'mailAddress=fuga@test.hoge.jp&password=password&csrfmiddlewaretoken=XXXXX' http://localhost:8000/login
# Existing ISBN
curl -X GET -b cookie.txt -d 'isbn=9784627705623' http://localhost:8000/search
# Not existing ISBN
curl -X GET -b cookie.txt -d 'isbn=8784627705623' http://localhost:8000/search
set +x
