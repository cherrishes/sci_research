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
    url(r'^job$', 'app.views.job', name='job'),
    url(r'^shiyanshiwenhua$', 'app.views.shiyanshiwenhua', name='shiyanshiwenhua'),
    url(r'^zhinengzhixing$', 'app.views.zhinengzhixing', name='zhinengzhixing'),
    url(r'^zuijiatuandui$', 'app.views.zuijiatuandui', name='zuijiatuandui'),
    url(r'^tebiegongxian$', 'app.views.tebiegongxian', name='tebiegongxian'),
    url(r'^quanjiafu$', 'app.views.quanjiafu', name='quanjiafu'),
    url(r'^juhuiyuanzu$', 'app.views.juhuiyuanzu', name='juhuiyuanzu'),
    url(r'^shenghuojianying$', 'app.views.shenghuojianying', name='shenghuojianying'),
    url(r'^xiaoyuanfengguang$', 'app.views.xiaoyuanfengguang', name='xiaoyuanfengguang'),
    url(r'^fengmiangushi$', 'app.views.fengmiangushi', name='fengmiangushi'),
    url(r'^chengyuanfengcai$', 'app.views.chengyuanfengcai', name='chengyuanfengcai'),
    url(r'^biyeshifen$', 'app.views.biyeshifen', name='biyeshifen'),
    url(r'^libiejiyu$', 'app.views.libiejiyu', name='libiejiyu'),
    url(r'^duzhewenzai$', 'app.views.duzhewenzai', name='duzhewenzai'),
    url(r'^jiaoxuegongzuo$', 'app.views.jiaoxuegongzuo', name='jiaoxuegongzuo'),
    url(r'^benkeshengdaoshi$', 'app.views.benkeshengdaoshi', name='benkeshengdaoshi'),
    url(r'^rengongzhineng$', 'app.views.rengongzhineng', name='rengongzhineng'),
    url(r'^more$', 'app.views.more', name='more'),
    url(r'^yangjiongshan$', 'app.views.yangjiongshan', name='yangjiongshan'),
    url(r'^zhaoyuhang$', 'app.views.zhaoyuhang', name='zhaoyuhang'),
    url(r'^zhangjing$', 'app.views.zhangjing', name='zhangjing'),
    url(r'^dingwei$', 'app.views.dingwei', name='dingwei'),
    url(r'^kuangye$', 'app.views.kuangye', name='kuangye'),
    url(r'^wangwei$', 'app.views.wangwei', name='wangwei'),
)
