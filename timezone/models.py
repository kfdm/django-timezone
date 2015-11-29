from django.db import models
import pytz


class Timezone(models.Model):
    owner = models.OneToOneField('auth.User', related_name='timezone', primary_key=True)
    timezone = models.CharField(max_length=32, choices=((tz, tz) for tz in pytz.common_timezones))
