from project.settings import *
import logging

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

SECRET_KEY = 'secret'  # Needed for drone

logging.disable(logging.CRITICAL)