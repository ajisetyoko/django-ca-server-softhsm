#!/bin/bash

# Do migration
python manage.py migrate
sleep 5

# Creating Admin
DJANGO_SUPERUSER_USERNAME=testuser \
DJANGO_SUPERUSER_PASSWORD=testpass \
DJANGO_SUPERUSER_EMAIL=test@mail.com \
python manage.py createsuperuser --noinput
sleep 5

# Do some initial process
python manage.py collectstatic

# Start Server
echo $ENV_STATUS
if [ $ENV_STATUS == 'PRODUCTION' ]
then
    echo "Deploy in production enviroment"
    gunicorn service.wsgi -b 0.0.0.0:8000
else
    echo "Deploy in developement enviroment"
    python manage.py runserver 0.0.0.0:8000
fi