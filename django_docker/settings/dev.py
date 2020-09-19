from .base import *  # noqa

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, 'config/envs/.env.dev'))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
