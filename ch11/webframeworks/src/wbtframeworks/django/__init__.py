import sys
import os
from django.urls import re_path
from django.conf import settings
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application


settings.configure(
    DEBUG=True,
    ROOT_URLCONF=sys.modules[__name__],
    ALLOWED_HOSTS=["httpbin.org"]
)


def home(request):
    return HttpResponse('Hello World')


urlpatterns = [
    re_path(r'^$', home),
    ]


def make_application():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
                          'wbtframeworks.django.settings')
    return get_wsgi_application()
