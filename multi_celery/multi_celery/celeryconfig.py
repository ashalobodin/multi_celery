import django
from django.core.exceptions import AppRegistryNotReady
from kombu import Exchange, Queue


try:
    from django.apps import apps

    apps.check_apps_ready()
except AppRegistryNotReady:
    django.setup()

BROKER_URL = 'redis://redis_test:6379'


CELERY_IMPORTS = (
    'multi_celery.tasks',
)

CELERY_RESULT_BACKEND = BROKER_URL

celery_general_queue = 'celery'

task_routes = ([
    ('multi_celery.tasks.*', {'queue': celery_general_queue}),
])

CELERY_QUEUES = (
    Queue(
        celery_general_queue,
        Exchange(name=celery_general_queue, type='direct'),
        routing_key=celery_general_queue),

)

CELERY_ROUTES = {
    'multi_celery.tasks.*': {
        'queue': celery_general_queue
    }
}


CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_DEFAULT_QUEUE = 'celery'
CELERY_DEFAULT_EXCHANGE = 'celery'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'celery'
