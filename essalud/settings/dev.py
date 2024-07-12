from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'ESSALUD',
        'USER': 'sa',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}

# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.backends.sqlite3',
#         # 'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASE_CONNECTION_POOLING = False

STATIC_URL = '/static/'