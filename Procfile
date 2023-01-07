release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn greenmark.wsgi --log-file - --log-level debug