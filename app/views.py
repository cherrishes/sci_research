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


def is_english(request):
    """
    判断是否英文访问
    :param request:
    :return:
    """

    if "HTTP_HOST" in request.META.keys():
        host = request.META["HTTP_HOST"].lower()

        if "en." in host or "localhost" in host:
            return True
    return False


def home(request):
    if is_mobile(request):
        return render(request, "mobile/home.html", locals())
    english = is_english(request)
    return render(request, "home.html", locals())


def member(request):
    english = is_english(request)
    return render(request, "member/member.html", locals())


def teacher(request):
    english = is_english(request)
    t = "member/teacher/teacher.html"
    return render(request, t, locals())


def member_teacher(request, name):
    english = is_english(request)
    t = "member/teacher/" + name + ".html"
    return render(request, t, locals())


def doctor(request):
    english = is_english(request)
    t = "member/dc/doctor.html"
    return render(request, t, locals())


def member_doctor(request, name):
    english = is_english(request)
    t = "member/dc/" + name + ".html"
    return render(request, t, locals())


def post_doctoral(request):
    english = is_english(request)
    t = "member/post_doctoral/post_doctoral.html"
    return render(request, t, locals())


def member_post_doctoral(request, name):
    english = is_english(request)
    t = "member/post_doctoral/" + name + ".html"
    return render(request, t, locals())


def postgraduate(request):
    english = is_english(request)
    t = "member/postgraduate/postgraduate.html"
    return render(request, t, locals())


def member_postgraduate(request, name):
    english = is_english(request)
    t = "member/postgraduate/" + name + ".html"
    return render(request, t, locals())


def undergraduate(request):
    english = is_english(request)
    t = "member/undergraduate/undergraduate.html"
    return render(request, t, locals())


def member_undergraduate(request, name):
    english = is_english(request)
    t = "member/undergraduate/" + name + ".html"
    return render(request, t, locals())


def scholars(request):
    english = is_english(request)
    t = "member/scholars/scholars.html"
    return render(request, t, locals())


def member_scholars(request, name):
    english = is_english(request)
    t = "member/scholars/" + name + ".html"
    return render(request, t, locals())


def more(request):
    english = is_english(request)
    return render(request, "more/more.html", locals())


def notice(request):
    english = is_english(request)
    return render(request, "more/notice.html", locals())


def team(request):
    english = is_english(request)
    return render(request, "more/team.html", locals())


def mrshen(request):
    english = is_english(request)
    return render(request, "member/teacher/mrshen.html", locals())


def about(request, uri):
    english = is_english(request)
    t = "about/"+uri+".html"
    return render(request, t, locals())


def research(request, uri):
    english = is_english(request)
    t = "research/"+uri+".html"
    return render(request, t, locals())


def achievement(request, uri):
    english = is_english(request)
    t = "achievement/"+uri+".html"
    return render(request, t, locals())


def culture(request, uri):
    english = is_english(request)
    t = "lab_culture/" + uri + ".html"
    return render(request, t, locals())


def activity(request, uri):
    english = is_english(request)
    t = "academic_activity/" + uri + ".html"
    return render(request, t, locals())


def chufang(request, uri):
    english = is_english(request)
    t = "xueshuhuodong/" + uri + ".html"
    return render(request, t, locals())


def work(request, uri):
    english = is_english(request)
    t = "teaching_work/" + uri + ".html"
    return render(request, t, locals())


def recruit(request, uri):
    english = is_english(request)
    t = "jobs/" + uri + ".html"
    return render(request, t, locals())


def news(request):
    english = is_english(request)
    t = "news/news.html"
    return render(request, t, locals())


def news_info(request, uri):
    english = is_english(request)
    t = "news/" + uri + ".html"
    return render(request, t, locals())