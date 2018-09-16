from datetime import timedelta


class CeleryConfig(dict):

    CELERYBEAT_SCHEDULE = {
        'task_add': {
            'task': 'proj.tasks.add',
            'schedule': timedelta(seconds=30),
            'args': (1, 2),
        }
    }

