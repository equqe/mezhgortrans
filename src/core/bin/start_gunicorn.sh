#!/bin/bash

python manage.py makemigrations && python manage.py migrate

exec gunicorn  -c "/app/core/gunicorn_config.py" core.wsgi
