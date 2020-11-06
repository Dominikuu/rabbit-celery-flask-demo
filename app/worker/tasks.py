import time
import random
import datetime
import json
from io import BytesIO
from celery import Celery, current_task
from celery.utils.log import get_task_logger

from celery.result import AsyncResult

from app.worker import celery

logger = get_task_logger(__name__)

def get_job(job_id):
    '''
    To be called from our web app.
    The job ID is passed and the celery job is returned.
    '''
    return AsyncResult(job_id, app=celery)

@celery.task
def long_time_task():
    logger.info('[task] long_time_task: start')
    time.sleep(2)
    logger.info('[task] long_time_task: finished')

@celery.task()
def get_data():
    logger.info('[task] get_data: start')
    current_task.update_state(state='PROGRESS', meta={'current':0.1})
    time.sleep(5)
    current_task.update_state(state='PROGRESS', meta={'current':0.3})
    time.sleep(5)
    current_task.update_state(state='PROGRESS', meta={'current':0.5})
    time.sleep(5)
    current_task.update_state(state='PROGRESS', meta={'current':0.8})
    time.sleep(5)
    logger.info('[task] get_data: finished')
    out = "SUCCESSFUL"
    return out
