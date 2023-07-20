from celery.utils.log import get_task_logger
from .models import Automation, ExecutionLog
from celery import shared_task
from celery.schedules import crontab
import requests
from datetime import datetime



@shared_task
def run_scraping(id):
    automation_instance = Automation.objects.get(id=id)
    try:
        response = requests.request(
            method=automation_instance.http_method,
            url=automation_instance.url,
            data=automation_instance.request_body
        )

        status_code = response.status_code
        html_content = response.text if status_code != 404 else 'Page not found'

        ExecutionLog.objects.create(
            automation=automation_instance,
            status_code=status_code,
            html_content=html_content,
            executed_at=datetime.now()
        )
    except ConnectionError:
        logger.info(f'error running automation with id {id}')
        ExecutionLog.objects.create(
            automation=automation_instance,
            status_code=500,
            html_content=f'Error connecting to {automation_instance.url}',
            executed_at=datetime.now()
        )