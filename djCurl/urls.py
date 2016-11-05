from django.conf.urls import include, url
from djCurl.views import *

urlpatterns = [
    url(r'^curl/$', getResult, name = 'getCurlResult'),
]
