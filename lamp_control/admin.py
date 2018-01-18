from django.contrib import admin

from lamp_control.models import Lamp
from lamp_control.models import Log

admin.site.register(Lamp)


class LogAdmin(admin.ModelAdmin):
    list_display = ["lamp", "timestamp", "hostname"]
    list_filter = ["lamp", "hostname"]
    date_hierarchy = "timestamp"


admin.site.register(Log, LogAdmin)
