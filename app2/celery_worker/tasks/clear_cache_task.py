from commons.celery_worker.app import CustomTask


def clear_cache_task_(self: CustomTask, id: str):
    self.redis_client.clear_cache(id)

