#!/bin/bash

set -x
curl -X GET -c cookie.txt http://localhost:8000/login/ | grep csrfmiddlewaretoken
curl -i -X POST -b cookie.txt -c cookie.txt -d 'mailAddress=fuga@test.hoge.jp&password=password&csrfmiddlewaretoken=XXXXX' http://localhost:8000/login
#curl -i -X POST -b cookie.txt -c cookie.txt -d 'isbn=9784627705623&csrfmiddlewaretoken=XXXXX' http://localhost:8000/search
curl -X GET -b cookie.txt -d 'isbn=8784627705623' http://localhost:8000/search
set +x
