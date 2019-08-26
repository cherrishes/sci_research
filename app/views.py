# !/bash/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

__author__ = 'rdy'


def is_mobile(request):
    """
    判断浏览器是否为移动设备浏览器
    :param request:
    :return:
    """
    if "HTTP_USER_AGENT" in request.META.keys():
        agent = request.META["HTTP_USER_AGENT"].lower()
        view = request.REQUEST.get("view", "")
        if "android" in agent or "mobile" in agent or "iemobile" in agent:
            if view != "pc":
                return True
    return False


def home(request):
    if is_mobile(request):
        return render(request, "mobile/home.html", locals())
    return render(request, "home.html", locals())


def member(request):
    return render(request, "member/member.html", locals())


def teacher(request):
    t = "member/teacher/teacher.html"
    return render(request, t, locals())


def member_teacher(request, name):
    t = "member/teacher/" + name + ".html"
    return render(request, t, locals())


def doctor(request):
    t = "member/dc/doctor.html"
    return render(request, t, locals())


def member_doctor(request, name):
    t = "member/dc/" + name + ".html"
    return render(request, t, locals())


def post_doctoral(request):
    t = "member/post_doctoral/post_doctoral.html"
    return render(request, t, locals())


def member_post_doctoral(request, name):
    t = "member/post_doctoral/" + name + ".html"
    return render(request, t, locals())


def postgraduate(request):
    t = "member/postgraduate/postgraduate.html"
    return render(request, t, locals())


def member_postgraduate(request, name):
    t = "member/postgraduate/" + name + ".html"
    return render(request, t, locals())


def undergraduate(request):
    t = "member/undergraduate/undergraduate.html"
    return render(request, t, locals())


def member_undergraduate(request, name):
    t = "member/undergraduate/" + name + ".html"
    return render(request, t, locals())


def scholars(request):
    t = "member/scholars/scholars.html"
    return render(request, t, locals())


def member_scholars(request, name):
    t = "member/scholars/" + name + ".html"
    return render(request, t, locals())


# def teacher(request):
#     return render(request, "member/teacher/teacher.html", locals())
#
#
# def postgraduate(request):
#     return render(request, "member/postgraduate/postgraduate.html", locals())
#
#
# def undergraduate(request):
#     return render(request, "member/undergraduate.html", locals())
#

#
#
# def rimler(request):
#     return render(request, "member/RIMLer.html", locals())


def xueshuchengguo(request):
    return render(request, "xueshuchengguo/xueshuchengguo.html", locals())


def xueshulunwen(request):
    return render(request, "xueshuchengguo/xueshulunwen.html", locals())


def liangdiangongzuo(request):
    return render(request, "xueshuchengguo/liangdiangongzuo.html", locals())


def fengmianjijin(request):
    return render(request, "xueshuchengguo/fengmianjijin.html", locals())


def zhuzuoyizhu(request):
    return render(request, "xueshuchengguo/zhuzuoyizhu.html", locals())


def famingzhuanli(request):
    return render(request, "xueshuchengguo/famingzhuanli.html", locals())


def xueshujiangli(request):
    return render(request, "xueshuchengguo/xueshujiangli.html", locals())


def daibiaoxinglunwen(request):
    return render(request, "xueshuchengguo/daibiaoxinglunwen.html", locals())


def lunwen2017(request):
    return render(request, "xueshuchengguo/lunwen2017.html", locals())


def lunwen2018(request):
    return render(request, "xueshuchengguo/lunwen2018.html", locals())


def lunwen2016(request):
    return render(request, "xueshuchengguo/lunwen2016.html", locals())


def xueshuhuodong(request):
    return render(request, "xueshuhuodong/xueshuhuodong.html", locals())


def job(request):
    return render(request, "jobs/job.html", locals())


def shiyanshiwenhua(request):
    return render(request, "shiyanshiwenhua/shiyanshiwenhua.html", locals())


def zhinengzhixing(request):
    return render(request, "shiyanshiwenhua/zhinengzhixing.html", locals())


def zuijiatuandui(request):
    return render(request, "shiyanshiwenhua/zuijiatuandui.html", locals())


def tebiegongxian(request):
    return render(request, "shiyanshiwenhua/tebiegongxian.html", locals())


def quanjiafu(request):
    return render(request, "shiyanshiwenhua/quanjiafu.html", locals())


def juhuiyuanzu(request):
    return render(request, "shiyanshiwenhua/juhuiyuanzu.html", locals())


def shenghuojianying(request):
    return render(request, "shiyanshiwenhua/shenghuojianying.html", locals())


def xiaoyuanfengguang(request):
    return render(request, "shiyanshiwenhua/xiaoyuanfengguang.html", locals())


def fengmiangushi(request):
    return render(request, "shiyanshiwenhua/fengmiangushi.html", locals())


def chengyuanfengcai(request):
    return render(request, "shiyanshiwenhua/chengyuanfengcai.html", locals())


def biyeshifen(request):
    return render(request, "shiyanshiwenhua/biyeshifen.html", locals())


def libiejiyu(request):
    return render(request, "shiyanshiwenhua/libiejiyu.html", locals())


def duzhewenzai(request):
    return render(request, "shiyanshiwenhua/duzhewenzai.html", locals())


def jiaoxuegongzuo(request):
    return render(request, "jiaoxuegongzuo/jiaoxuegongzuo.html", locals())


def benkeshengdaoshi(request):
    return render(request, "jiaoxuegongzuo/benkeshengdaoshi.html", locals())


def rengongzhineng(request):
    return render(request, "jiaoxuegongzuo/rengongzhineng.html", locals())


def more(request):
    return render(request, "more/more.html", locals())


def yangjiongshan(request):
    return render(request, "member/postgraduate/yangjiongshan.html", locals())


def zhaoyuhang(request):
    return render(request, "member/yilikai/zhaoyuhang.html", locals())


def zhangjing(request):
    return render(request, "member/yilikai/zhangjing.html", locals())


def dingwei(request):
    return render(request, "member/yilikai/dingwei.html", locals())


def kuangye(request):
    return render(request, "member/postgraduate/kuangye.html", locals())


def wangwei(request):
    return render(request, "member/yilikai/wangwei.html", locals())


def mrshen(request):
    return render(request, "member/teacher/mrshen.html", locals())


def yilikai(request):
    return render(request, "member/yilikai/yilikai.html", locals())





def sunhong(request):
    return render(request, "member/postgraduate/sunhong.html", locals())


def zhangsai(request):
    return render(request, "member/postgraduate/zhangsai.html", locals())


def zhoujincheng(request):
    return render(request, "member/postgraduate/zhoujincheng.html", locals())


def zhouyi(request):
    return render(request, "member/postgraduate/zhouyi.html", locals())


def d416(request):
    return render(request, "news/d416.html", locals())


def d1228(request):
    return render(request, "news/d1228.html", locals())


def d1220(request):
    return render(request, "news/d1220.html", locals())


def chenkang(request):
    return render(request, "member/postgraduate/chenkang.html", locals())


def liyong(request):
    return render(request, "member/postgraduate/liyong.html", locals())


def jinchunlei(request):
    return render(request, "member/postgraduate/jinchunlei.html", locals())


def abdulazeez(request):
    return render(request, "member/postgraduate/abdulazeez.html", locals())


def d722(request):
    return render(request, "news/d722.html", locals())


def d1125(request):
    return render(request, "news/d1125.html", locals())


def d419(request):
    return render(request, "news/d419.html", locals())


def d624(request):
    return render(request, "news/d624.html", locals())


def d825(request):
    return render(request, "news/d825.html", locals())


def about(request, uri):

    t = "about/"+uri+".html"
    return render(request, t, locals())


def research(request, uri):

    t = "keyanfangxiang/"+uri+".html"
    return render(request, t, locals())


def achievement(request, uri):

    t = "achievement/"+uri+".html"
    return render(request, t, locals())


def culture(request, uri):
    t = "shiyanshiwenhua/" + uri + ".html"
    return render(request, t, locals())


def activity(request, uri):
    t = "xueshuhuodong/" + uri + ".html"
    return render(request, t, locals())


def chufang(request, uri):
    t = "xueshuhuodong/" + uri + ".html"
    return render(request, t, locals())


def work(request, uri):
    t = "jiaoxuegongzuo/" + uri + ".html"
    return render(request, t, locals())


def recruit(request, uri):
    t = "jobs/" + uri + ".html"
    return render(request, t, locals())


def news(request):
    t = "news/news.html"
    return render(request, t, locals())