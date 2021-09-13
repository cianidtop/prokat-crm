from django.contrib import admin
from .models import Tech


class TechAdmin(admin.ModelAdmin):
    list_display = ("tech", "start_time")

admin.site.register(Tech , TechAdmin)