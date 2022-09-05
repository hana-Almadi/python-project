from app2.app.config import config
from commons.celery_worker.app import init_app

app = init_app(config)

app.conf.beat_schedule = {
    "beat1": {
        "task": "app2.celery_worker.worker.clear_cache_task",
        "schedule": 60,
        "args": ("1",),
    },
}
