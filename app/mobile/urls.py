# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


app_patterns = patterns(
    'app.mobile.views',
    url(r'^$', "home"),
    url(r'^about$', "about"),
    url(r'^research$', "research"),
    url(r'^result$', "result"),
    url(r'^member$', "member"),
    url(r'^culture$', "culture"),
    url(r'^news/(?P<uri>\S+)$', "news_info"),
    url(r'^member/postgraduate/(?P<name>\S+)$', "member_postgraduate"),
    url(r'^member/teacher/(?P<name>\S+)$', "member_teacher"),
)
