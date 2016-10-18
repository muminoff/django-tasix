SECRET_KEY = 'tasix'

MIDDLEWARE_CLASSES = (
    'tasix.middleware.TasixMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    },
}
