python manage.py migrate
sleep 5
DJANGO_SUPERUSER_USERNAME=testuser \
DJANGO_SUPERUSER_PASSWORD=testpass \
DJANGO_SUPERUSER_EMAIL=test@mail.com \
python manage.py createsuperuser --noinput
sleep 5
gunicorn service.wsgi