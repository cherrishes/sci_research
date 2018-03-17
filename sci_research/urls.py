from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sci_research.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^member$', 'app.views.member',name='member'),
    url(r'^teacher$', 'app.views.teacher', name='teacher'),
    url(r'^postgraduate$', 'app.views.postgraduate', name='postgraduate'),
    url(r'^undergraduate$', 'app.views.undergraduate', name='undergraduate'),
    url(r'^assistant$', 'app.views.assistant', name='assistant'),
    url(r'^RIMLer$', 'app.views.RIMLer', name='RIMLer'),
    url(r'^xueshuchengguo$', 'app.views.xueshuchengguo', name='xueshuchengguo'),
    url(r'^xueshulunwen$', 'app.views.xueshulunwen', name='xueshulunwen'),
    url(r'^liangdiangongzuo$', 'app.views.liangdiangongzuo', name='liangdiangongzuo'),
    url(r'^fengmianjijin$', 'app.views.fengmianjijin', name='fengmianjijin'),
    url(r'^zhuzuoyizhu$', 'app.views.zhuzuoyizhu', name='zhuzuoyizhu'),
    url(r'^famingzhuanli$', 'app.views.famingzhuanli', name='famingzhuanli'),
    url(r'^xueshujiangli$', 'app.views.xueshujiangli', name='xueshujiangli'),
    url(r'^daibiaoxinglunwen$', 'app.views.daibiaoxinglunwen', name='daibiaoxinglunwen'),
    url(r'^lunwen2018$', 'app.views.lunwen2018', name='lunwen2018'),
    url(r'^lunwen2017$', 'app.views.lunwen2017', name='lunwen2017'),
    url(r'^lunwen2016$', 'app.views.lunwen2016', name='lunwen2016'),
    url(r'^keyanfangxiang$', 'app.views.keyanfangxiang', name='keyanfangxiang'),
    url(r'^chengdanxiangmu$', 'app.views.chengdanxiangmu', name='chengdanxiangmu'),
    url(r'^yiqishebei$', 'app.views.yiqishebei', name='yiqishebei'),
    url(r'^xiangguanzazhi$', 'app.views.xiangguanzazhi', name='xiangguanzazhi'),
    url(r'^xueshuhuodong$', 'app.views.xueshuhuodong', name='xueshuhuodong'),
)
