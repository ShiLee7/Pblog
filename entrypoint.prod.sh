#!/usr/bin/env bash
set -o errexit
set -o pipefail
set -o nounset

python manage.py collectstatic --noinput
python manage.py migrate --noinput
exec gunicorn Pblog.wsgi:application \
     --bind 0.0.0.0:8000 \
     --workers 3 \
     --timeout 60