COMPRESS_PRECOMPILERS = (('text/less', 'c://less/lessc {infile}'),)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}

CACHE_BACKEND = CACHES["default"]["BACKEND"]