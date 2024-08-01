#!/usr/bin/env bash
# Exit on error: the script will terminate if any command exits with a non-zero status
set -o errexit

# Install the necessary dependencies listed in requirements.txt using pip.
pip install -r requirements.txt

# Convert static asset files
python3 manage.py collectstatic --no-input

# Apply any outstanding database migrations
python3 manage.py migrate
