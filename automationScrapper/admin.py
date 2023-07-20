from django.contrib import admin
from .models import Automation, ExecutionLog, ScrapperRobot

class AutomationInline(admin.TabularInline):
    model = Automation
    extra = 1
    
class ScraperRobotAdmin(admin.ModelAdmin):
    inlines = [AutomationInline]

class ExecutionLogAdmin(admin.ModelAdmin):
    readonly_fields = ('automation', 'status_code', 'html_content', 'executed_at')

admin.site.register(Automation)
admin.site.register(ScrapperRobot, ScraperRobotAdmin)
admin.site.register(ExecutionLog, ExecutionLogAdmin)