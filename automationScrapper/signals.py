from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Automation

@receiver(post_save, sender=Automation)
def scheduling_task(sender, instance, created, **kwargs):
    print(created)