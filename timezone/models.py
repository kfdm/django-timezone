import datetime

from django.db import models

import pytz


class Timezone(models.Model):
    owner = models.OneToOneField('auth.User', related_name='timezone', primary_key=True, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=32, default='UTC')

    def __str__(self):
        return self.timezone

    @property
    def tzinfo(self):
        return pytz.timezone(self.timezone)

    def now(self):
        return datetime.datetime.now(tz=self.tzinfo)

    @classmethod
    def for_user(cls, owner):
        obj, created = cls.objects.get_or_create(owner=owner)
        return obj
