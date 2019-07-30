from django.conf.urls import url
from .views import index, dishes, dish, new_dish
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #Home page
    url(r'^$', index, name='index'),
    url(r'^dishes/$', dishes, name='dishes'),
    url(r'^dishes/(?P<dish_id>\d+)/$', dish, name='dish'),
    #page for adding a new topic
    url(r'^new_dish/$', new_dish, name='new_dish'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
