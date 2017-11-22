from django.utils import timezone

import pytz

from timezone.models import Timezone


class TimezoneMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            timezone.deactivate()
            return

        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
            return

        tz, created = Timezone.objects.get_or_create(owner=request.user)
        request.session['django_timezone'] = tz.timezone
        timezone.activate(pytz.timezone(tz.timezone))

    def process_response(self, request, response):
        response['X-Timezone'] = request.session.get('django_timezone')
        return response
