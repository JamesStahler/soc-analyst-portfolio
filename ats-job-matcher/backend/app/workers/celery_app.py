from celery import Celery

from app.core.config import settings

celery_app = Celery("ats_job_matcher", broker=settings.redis_url, backend=settings.redis_url)

celery_app.conf.task_routes = {
    "app.workers.tasks.process_job_search": {"queue": "job-search"},
    "app.workers.tasks.generate_documents_task": {"queue": "document-gen"},
}
