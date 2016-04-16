from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.list, name='list'),
    url(r'^delete/(?P<songId>[0-9]+)/$',
        views.delete, name='delete')
]
