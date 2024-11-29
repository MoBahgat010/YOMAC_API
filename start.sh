#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn api.wsgi:application --bind 0.0.0.0:$PORT