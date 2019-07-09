from django.conf.urls import url

from .views import index

urlpatterns = [
    #Home page
    url(r'^home$', index, name='index'),
]
