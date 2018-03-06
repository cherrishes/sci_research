from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sci_research.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', 'app.views.home', name='home'),
    url(r'^member$', 'app.views.member',name='member'),
    url(r'^teacher$', 'app.views.teacher', name='teacher'),
    url(r'^postgraduate$', 'app.views.postgraduate', name='postgraduate'),
    url(r'^undergraduate$', 'app.views.undergraduate', name='undergraduate'),
    url(r'^assistant$', 'app.views.assistant', name='assistant'),
    url(r'^RIMLer$', 'app.views.RIMLer', name='RIMLer'),
)
