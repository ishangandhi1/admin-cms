from settings import PROJECT_ROOT
import os

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2", # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'heroku_deploy', # Or path to database file if using sqlite3.
        'USER': 'heroku7692', # Not used with sqlite3.
        'PASSWORD': 'Okhli123!', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432', # Set to empty string for default. Not used with sqlite3.
    }
}