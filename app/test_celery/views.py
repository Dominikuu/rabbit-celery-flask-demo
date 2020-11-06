import json
from flask import jsonify, request, render_template

from app.worker import tasks
from app.test_celery import test_celery


@test_celery.route('/', methods=['GET'])
def index():
    result = tasks.long_time_task.delay()
    return jsonify(msg='request received', result_id=result.id)


@test_celery.route('/progress/<job_id>', methods=['GET'])
def progress(job_id: str) -> str:
    if job_id:
        job = tasks.get_job(job_id)
        if job.state == 'PROGRESS':
            return json.dumps(dict(
                state=job.state,
                progress=job.result['current'],
            ))
        elif job.state == 'SUCCESS':
            return json.dumps(dict(
                state=job.state,
                progress=1.0,
            ))
    return '{}'

@test_celery.route('/task', methods=['GET'])
def get_task():
    job = tasks.get_data.delay()
    return render_template('index.html', JOBID=job.id)