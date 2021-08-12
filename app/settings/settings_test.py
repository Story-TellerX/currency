from settings.settings import *  # noqa

DEBUG = False
CELERY_TASK_ALWAYS_EAGER = True

TEST_MEMCACHE = False

CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        },
}
