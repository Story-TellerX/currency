from settings.settings import *  # noqa

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DEBUG = False
CELERY_TASK_ALWAYS_EAGER = True
