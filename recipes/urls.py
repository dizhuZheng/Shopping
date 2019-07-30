from django.conf.urls import url
from .views import index, dishes, dish, upload_img, show_img
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #Home page
    url(r'^$', index, name='index'),
    url(r'^dishes/$', dishes, name='dishes'),
    url(r'^dishes/(?P<dish_id>\d+)/$', dish, name='dish'),
    url(r'^upload/$', upload_img),
    url(r'^show/$', show_img),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
