from django.db import models


class Timezone(models.Model):
    owner = models.OneToOneField('auth.User', related_name='timezone', primary_key=True, on_delete=models.CASCADE)
    timezone = models.CharField(max_length=32, default='UTC')

    def __str__(self):
        return self.timezone
