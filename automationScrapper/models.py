from django.db import models

from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ScrapperRobot(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Automation(TimeStampedModel):
    HTTPChoices = [
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
    ]

    FrequencyChoices = [
        ('Hourly', 'Hourly'),
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
    ]
    id_scraper_robot = models.ForeignKey(ScrapperRobot, on_delete=models.CASCADE)
    url = models.URLField()
    http_method = models.CharField(max_length=10, default="GET", choices=HTTPChoices)
    request_body = models.TextField(blank=True)
    scheduled_time = models.TimeField()
    scheduled_frequency = models.CharField(max_length=10, default="Hourly", choices=FrequencyChoices)
   

    def __str__(self):
        return f'{self.url} - {self.http_method} ({self.scheduled_time})'
    


class ExecutionLog(TimeStampedModel):
    automation = models.ForeignKey(Automation, on_delete=models.CASCADE)
    executed_at = models.DateTimeField(auto_now_add=True)
    html_content = models.TextField()
    status_code = models.IntegerField()

    def __str__(self):
        return f'{self.automation.url} ({self.automation.http_method}) - {self.executed_at}'
 