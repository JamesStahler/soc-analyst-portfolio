from app.workers.celery_app import celery_app


@celery_app.task
def process_job_search(payload: dict) -> dict:
    # Placeholder async/offline processing for heavy search + crawling workflows.
    return {"status": "queued", "payload": payload}


@celery_app.task
def generate_documents_task(payload: dict) -> dict:
    # Placeholder task for premium priority generation.
    return {"status": "queued", "payload": payload}
