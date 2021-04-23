from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
'periodic_send_email': {
    'task': 'cloud_app.tasks.periodic_send_email',
    'schedule': crontab(minute="*/15"),
},
}