from django.conf.urls import url
from .views import index, dishes, dish

urlpatterns = [
    #Home page
    url(r'^$', index, name='index'),
    url(r'^dishes/$', dishes, name='dishes'),
    url(r'^dishes/(?P<dish_id>\d+)/$', dish, name='dish'),

]
