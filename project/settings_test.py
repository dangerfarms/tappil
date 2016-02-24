from project.settings import *

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

DATABASE_URL = 'postgis://postgres:postgres@db:5432/postgres'

SECRET_KEY = 'secret'