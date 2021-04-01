import django
from django.core.exceptions import AppRegistryNotReady


# try:
#     from django.apps import apps
#     apps.check_apps_ready()
# except AppRegistryNotReady:
#     django.setup()

celery_general_queue = 'celery'

accept_content = ['json']

broker_url = 'redis://redis_test:6379'

imports = (
    'multi_celery.tasks',
)

result_serializer = 'json'
result_backend = broker_url

task_routes = ([
    ('multi_celery.tasks.*', {'queue': celery_general_queue}),
])

task_create_missing_queues = True
task_default_queue = 'celery'
task_default_exchange = 'celery'
task_default_exchange_type = 'direct'
task_default_routing_key = 'celery'
task_serializer = 'json'
