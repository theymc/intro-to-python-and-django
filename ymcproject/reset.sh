rm horses.db
python manage.py syncdb --noinput
python manage.py runserver
