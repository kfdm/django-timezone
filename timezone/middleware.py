import pytz

from django.utils import timezone
from timezone.models import Timezone


class TimezoneMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            return

        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            tzname = Timezone.objects.filter(owner=request.user)
            if tzname:
                request.session['django_timezone'] = tzname[0].timezone
                timezone.activate(pytz.timezone(tzname[0].timezone))
            else:
                timezone.deactivate()
