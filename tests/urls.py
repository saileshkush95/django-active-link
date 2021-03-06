# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url
from django.views.generic import View


urlpatterns = [
    url(r'^simple/$', View.as_view(), name='simple'),
    url(r'^multiple/$', View.as_view(), name='multiple'),
    url(r'^simple/action/$', View.as_view(), name='simple-action'),
    url(r'^multiple/action/$', View.as_view(), name='multiple-action'),
    url(r'^other/action/$', View.as_view(), name='other-action'),
    url(r'^detailed/action/(?P<pk>[0-9]+)/$', View.as_view(), name='detailed-action')
]
