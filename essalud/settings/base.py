
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-38n$r!&k3vlol3m81p3e=9!qz+-18$i%zn@f5)x+^d9!)&6fd('

AUTH_USER_MODEL = 'person.User'

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'import_export',
]

LOCAL_APPS = [
    'apps.dashboard',
    'apps.follow_up',
    'apps.packages',
    'apps.boards',
    'apps.main',
    'apps.person',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

LOGIN_URL = '/'
LOGIN_REDIRECT_URL ="/home/"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'essalud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'essalud.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_COOKIE_AGE = 7200 # set just 10 seconds to test
SESSION_SAVE_EVERY_REQUEST = True

STATIC_URL = '/static/'

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]



# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'