from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'sci_research.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'app.views.home', name='home'),
                       url(r'^member$', 'app.views.member', name='member'),
                       url(r'^member/teacher$', 'app.views.teacher'),
                       url(r'^member/teacher/(?P<name>\S+)$', 'app.views.member_teacher'),
                       url(r'^member/scholars', 'app.views.scholars'),
                       url(r'^member/scholars/(?P<name>\S+)$', 'app.views.member_scholars'),
                       url(r'^member/post_doctoral', 'app.views.post_doctoral'),
                       url(r'^member/post_doctoral/(?P<name>\S+)$', 'app.views.member_post_doctoral'),
                       url(r'^member/doctor', 'app.views.doctor'),
                       url(r'^member/doctor/(?P<name>\S+)$', 'app.views.member_doctor'),
                       url(r'^member/postgraduate$', 'app.views.postgraduate'),
                       url(r'^member/postgraduate/(?P<name>\S+)$', 'app.views.member_postgraduate'),
                       url(r'^member/undergraduate', 'app.views.undergraduate'),
                       url(r'^member/undergraduate/(?P<name>\S+)$', 'app.views.member_undergraduate'),


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
                       # url(r'^keyanfangxiang$', 'app.views.keyanfangxiang', name='keyanfangxiang'),
                       # url(r'^chengdanxiangmu$', 'app.views.chengdanxiangmu', name='chengdanxiangmu'),
                       # url(r'^yiqishebei$', 'app.views.yiqishebei', name='yiqishebei'),
                       # url(r'^xiangguanzazhi$', 'app.views.xiangguanzazhi', name='xiangguanzazhi'),
                       url(r'^xueshuhuodong$', 'app.views.xueshuhuodong', name='xueshuhuodong'),

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


                       url(r'^dc$', 'app.views.dc', name='dc'),
                       url(r'^sunhong$', 'app.views.sunhong', name='sunhong'),
                       url(r'^zhangsai$', 'app.views.zhangsai', name='zhangsai'),
                       url(r'^zhoujincheng$', 'app.views.zhoujincheng', name='zhoujincheng'),
                       url(r'^zhouyi$', 'app.views.zhouyi', name='zhouyi'),
                       url(r'^d416$', 'app.views.d416', name='d416'),
                       url(r'^d1228$', 'app.views.d1228', name='d1228'),
                       url(r'^d1220$', 'app.views.d1220', name='d1220'),
                       url(r'^chenkang$', 'app.views.chenkang', name='chenkang'),
                       url(r'^liyong$', 'app.views.liyong', name='liyong'),
                       url(r'^jinchunlei$', 'app.views.jinchunlei', name='jinchenlei'),
                       url(r'^abdulazeez$', 'app.views.abdulazeez', name='abdulazeez'),
                       url(r'^d722$', 'app.views.d722', name='d722'),
                       url(r'^d1125$', 'app.views.d1125', name='d1125'),
                       url(r'^d419$', 'app.views.d419', name='d419'),
                       url(r'^d624$', 'app.views.d624', name='d624'),
                       url(r'^d825$', 'app.views.d825', name='d825'),

                       url(r'^about/(?P<uri>\S+)$', "app.views.about"),
                       url(r'^research/(?P<uri>\S+)$', "app.views.research"),
                       url(r'^ach/(?P<uri>\S+)$', "app.views.achievement"),
                       url(r'^culture/(?P<uri>\S+)$', "app.views.culture"),
                       url(r'^activity/(?P<uri>\S+)$', "app.views.activity"),
                       url(r'^chufang/(?P<uri>\S+)$', "app.views.chufang"),
                       url(r'^work/(?P<uri>\S+)$', "app.views.work"),
                       url(r'^recruit/(?P<uri>\S+)$', "app.views.recruit"),
                       url(r'^news$', "app.views.news"),
                       url(r'^news/(?P<uri>\S+)$', "app.views.recruit"),
                       )
