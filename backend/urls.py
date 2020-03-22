from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        r'the-coco-cabana/?',
        RedirectView.as_view(url=settings.COCO_CABANA_HANGOUT_URL),
    ),
]
