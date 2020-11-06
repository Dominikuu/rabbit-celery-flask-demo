from app import make_celery_app

celery = make_celery_app()

from app.worker import tasks

