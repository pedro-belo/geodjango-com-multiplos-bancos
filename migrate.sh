python manage.py makemigrations
python manage.py migrate --database=default users
python manage.py migrate --database=default admin
python manage.py migrate --database=default sessions
python manage.py migrate --database=default core
python manage.py migrate --database=geo_db geo_app
python manage.py loaddata core/fixtures/cities.json --database=default
python manage.py loaddata geo_app/fixtures/municipios.json --database=geo_db
