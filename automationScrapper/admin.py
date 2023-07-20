from django.contrib import admin
from .models import Automation, ExecutionLog, ScraperRobot

class ExecutionLogAdmin(admin.ModelAdmin):
    readonly_fields = ('automation', 'status_code', 'html_content', 'executed_at')

admin.site.register(Automation)
admin.site.register(ScraperRobot)
admin.site.register(ExecutionLog, ExecutionLogAdmin)