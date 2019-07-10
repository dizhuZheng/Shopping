from django.conf.urls import url

from .views import index

urlpatterns = [
    #Home page
    url(r'^$', index, name='index'),
]
