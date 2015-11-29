from django.contrib import admin

from timezone.models import Timezone

class TimezoneAdmin(admin.ModelAdmin):
    list_display = ('owner', 'timezone')

admin.site.register(Timezone, TimezoneAdmin)
