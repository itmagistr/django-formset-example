from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^zone/(?P<zone_name>[\w ]+)$', views.manage_resources, name='manage-resources'),
]
