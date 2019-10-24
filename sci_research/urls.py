from django.conf.urls import patterns, include, url
from django.contrib import admin

from app.mobile.urls import app_patterns

urlpatterns = patterns('',

                       url(r'^app/', include(app_patterns)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'app.views.home', name='home'),
                       url(r'^member$', 'app.views.member', name='member'),
                       url(r'^member/teacher$', 'app.views.teacher'),
                       url(r'^member/teacher/(?P<name>\S+)$', 'app.views.member_teacher'),
                       url(r'^member/scholars$', 'app.views.scholars'),
                       url(r'^member/scholars/(?P<name>\S+)$', 'app.views.member_scholars'),
                       url(r'^member/post_doctoral$', 'app.views.post_doctoral'),
                       url(r'^member/post_doctoral/(?P<name>\S+)$', 'app.views.member_post_doctoral'),
                       url(r'^member/doctor$', 'app.views.doctor'),
                       url(r'^member/doctor/(?P<name>\S+)$', 'app.views.member_doctor'),
                       url(r'^member/postgraduate$', 'app.views.postgraduate'),
                       url(r'^member/postgraduate/(?P<name>\S+)$', 'app.views.member_postgraduate'),
                       url(r'^member/undergraduate$', 'app.views.undergraduate'),
                       url(r'^member/undergraduate/(?P<name>\S+)$', 'app.views.member_undergraduate'),

                       url(r'^more$', 'app.views.more', name='more'),
                       url(r'^notice$', 'app.views.notice', name='notice'),
                       url(r'^team$', 'app.views.team', name='team'),

                       url(r'^about/(?P<uri>\S+)$', "app.views.about"),
                       url(r'^research/(?P<uri>\S+)$', "app.views.research"),
                       url(r'^ach/(?P<uri>\S+)$', "app.views.achievement"),
                       url(r'^culture/(?P<uri>\S+)$', "app.views.culture"),
                       url(r'^activity/(?P<uri>\S+)$', "app.views.activity"),
                       url(r'^chufang/(?P<uri>\S+)$', "app.views.chufang"),
                       url(r'^work/(?P<uri>\S+)$', "app.views.work"),
                       url(r'^recruit/(?P<uri>\S+)$', "app.views.recruit"),
                       url(r'^news$', "app.views.news"),
                       url(r'^news/(?P<uri>\S+)$', "app.views.news_info"),
                       )
