from django import forms
from django.contrib import admin

import pytz

from timezone.models import Timezone


class TimezoneForm(forms.ModelForm):
    timezone = forms.ChoiceField(
        choices=((tz, tz) for tz in pytz.common_timezones)
    )
    class Meta:
        model = Timezone
        fields = ['owner', 'timezone']


@admin.register(Timezone)
class TimezoneAdmin(admin.ModelAdmin):
    list_display = ('owner', 'timezone')
    form = TimezoneForm
