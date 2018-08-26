# !/bash/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

__author__ = 'rdy'


def home(request):
    return render(request, "home.html", locals())


def member(request):
    return render(request, "member/member.html", locals())


def teacher(request):
    return render(request, "member/teacher/teacher.html", locals())


def postgraduate(request):
    return render(request, "member/postgraduate/postgraduate.html", locals())


def undergraduate(request):
    return render(request, "member/undergraduate.html", locals())


def assistant(request):
    return render(request, "member/dc/dc.html", locals())


def rimler(request):
    return render(request, "member/RIMLer.html", locals())


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


def keyanfangxiang(request):
    return render(request, "keyanfangxiang/keyanfangxiang.html", locals())


def chengdanxiangmu(request):
    return render(request, "keyanfangxiang/chengdanxiangmu.html", locals())


def yiqishebei(request):
    return render(request, "keyanfangxiang/yiqishebei.html", locals())


def xiangguanzazhi(request):
    return render(request, "keyanfangxiang/xiangguanzazhi.html", locals())


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


def dc(request):
    return render(request, "member/dc/dc.html", locals())


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
