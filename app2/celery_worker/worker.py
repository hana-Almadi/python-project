from app2.app.config import config
from commons.celery_worker.app import CustomTask, init_app

from .tasks.clear_cache_task import clear_cache_task_

celery = init_app(config=config)


@celery.task(bind=True)
def clear_cache_task(self: CustomTask, *args, **kwargs) -> str:
    return clear_cache_task_(self, *args, **kwargs)
