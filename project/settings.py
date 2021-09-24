import os
# from dotenv import load_dotenv
from environs import Env

env = Env()
env.read_env()
# load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env.str('HOST'),
        'PORT': env.str('PORT'),
        'NAME': env.str('NAME'),
        'USER': env.str('DBUSER'),
        'PASSWORD': env.str('PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

DEBUG = env.bool('DEBUG')

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True