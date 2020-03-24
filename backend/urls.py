from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import RedirectView

from backend.app.views import ClubhouseView, FrontendView


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'the-coco-cabana/?', ClubhouseView.as_view()),
    re_path(r'^', FrontendView.as_view()),
]
