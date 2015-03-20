rm db.sqlite3
./manage.py makemigrations
./manage.py migrate
./manage.py loaddata cities
./manage.py loaddata walks
