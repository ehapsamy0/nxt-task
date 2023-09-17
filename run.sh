python manage.py migrate
python manage.py test
python manage.py runserver 0.0.0.0:8000
# gunicorn well_medic.wsgi:application --bind 0.0.0.0:8000
