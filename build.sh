#!/usr/bin/env bash
# exit on error
set -o errexit

# Force pip to install all requirements into the container
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate



#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py create_admin



#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Built-in Django command to create superuser without interactive prompts
python manage.py createsuperuser --no-input || true