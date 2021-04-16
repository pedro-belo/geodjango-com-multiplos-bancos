#!/bin/sh
mkdir -p /app/staticfiles
python manage.py collectstatic --noinput
sh migrate.sh
