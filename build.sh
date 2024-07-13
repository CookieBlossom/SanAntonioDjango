#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python3 manage.py collectstatic --noinput
python3 manage.py migrate
python3 manage.py runscript init_superuser -v3