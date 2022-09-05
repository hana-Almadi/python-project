from app1.app.config import config
from commons.celery_worker.app import init_app

app = init_app(config)

app.conf.beat_schedule = {
    "beat1": {
        "task": "app1.celery_worker.worker.task1",
        "schedule": 60,
        "args": (2,),
    },
}
