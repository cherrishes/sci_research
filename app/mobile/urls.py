# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


app_patterns = patterns(
    'app.mobile.views',
    url(r'^$', "home"),
    url(r'^about$', "about"),
    url(r'^research$', "research"),
    url(r'^result$', "result"),
)
