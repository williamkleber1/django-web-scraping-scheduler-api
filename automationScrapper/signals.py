from django.db.models.signals import post_save
from django.dispatch import receiver
from celery.schedules import crontab


from .models import Automation
import json
from django_celery_beat.models import CrontabSchedule, PeriodicTask

@receiver(post_save, sender=Automation)
def scheduling_task(sender, instance, created, **kwargs):
    print(created)
    tasks = PeriodicTask.objects.filter(name=f'{instance.url}-{instance.http_method}-{instance.id_scraper_robot.id}')
    print(tasks)
    if created and not tasks:
        data = instance.get_cron_schedule()

        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=data['minute'],
            hour=data['hour'],
            day_of_week=data['day_of_week'],
            day_of_month=data['day_of_month'],
            month_of_year=data['month_of_year'],
        )
        print(f'{instance.url}-{instance.http_method}-{instance.id_scraper_robot.id}')
        PeriodicTask.objects.create(
            crontab=schedule,
            name=f'{instance.url}-{instance.http_method}-{instance.id_scraper_robot.id}',
            task='automationScrapper.tasks.run_scraping',
            args=json.dumps([instance.id])
        )
    else:
        data = instance.get_cron_schedule()

        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute=data['minute'],
            hour=data['hour'],
            day_of_week=data['day_of_week'],
            day_of_month=data['day_of_month'],
            month_of_year=data['month_of_year'],
        )

        PeriodicTask.objects.filter(args=json.dumps([instance.id])).update(
            crontab=schedule
        )
    