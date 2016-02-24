DATABASE_URL = 'postgis://postgres:postgres@db:5432/postgres'

from project.settings import *

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

SECRET_KEY = 'secret'