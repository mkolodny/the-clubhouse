from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import View

import pytz


class FrontendView(View):
    
    def get(self, *args, **kwargs):
        with open(settings.FRONTEND_INDEX) as f:
            html = f.read()
            return HttpResponse(html)


class ClubhouseView(View):

    def get(self, *args, **kwargs):
        pt = pytz.timezone('US/Pacific')
        now = timezone.localtime(timezone=pt)
        six_thirty = timezone.localtime(timezone=pt).replace(
            hour=17,
            minute=30,
        )
        seven_thirty = timezone.localtime(timezone=pt).replace(
            hour=18,
            minute=30,
        )
        if six_thirty <= now < seven_thirty:
            # The clubhouse is open!
            return HttpResponseRedirect(settings.COCO_CABANA_HANGOUT_URL)
        else:
            # The clubhouse is closed :(
            with open(settings.FRONTEND_INDEX) as f:
                html = f.read()
                return HttpResponse(html)