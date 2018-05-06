# Coretabs Django Workshop
[Workshop Index](https://forums.coretabs.net/t/django/58)

## Lesson 01
### Install Last Version of Django
    pip install django

### Check Your Django Version, or Check if Django is Installed
    python -m django --version

### Start a New Project
    django-admin startproject coretabs

### Run Development Server
    python manage.py runserver

## Lesson 02
### Start a New Application
    python manage.py startapp shop

### Create migrations files for all apps, you can specify one or more applications
    python manage.py makemigrations [app] [app]

### Apply Migrations to Database
    python manage.py migrate