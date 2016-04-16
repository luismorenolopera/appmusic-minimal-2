# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('myproject.myapp.views',
                       url(r'^list/$', 'list', name='list'),
                       url(r'^delete/(?P<songId>[0-9]+)/$',
                           views.delete, name='delete')
                       )
