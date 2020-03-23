from django.conf import settings
from django.http import HttpResponse
from django.views import View


class FrontendView(View):
    
    def get(self, *args, **kwargs):
        with open(settings.FRONTEND_INDEX) as f:
            html = f.read()
            return HttpResponse(html)
