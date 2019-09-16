# -*- coding: utf-8 -*-
from django.shortcuts import render

__author__ = 'rdy'


def home(request):
    return render(request, "mobile/home.html", locals())


def about(request):
    return render(request, "mobile/about/about.html", locals())


def research(request):
    return render(request, "mobile/research.html", locals())


def result(request):
    return render(request, "mobile/result.html", locals())


def member(request):
    return render(request, "mobile/member.html", locals())


def culture(request):
    return render(request, "mobile/culture.html", locals())


def news_info(request, uri):
    t = "news/" + uri+"-mobile.html"
    return render(request, t, locals())


def member_postgraduate(request, name):
    t = "mobile/member/postgraduate/" + name + ".html"
    return render(request, t, locals())


def member_teacher(request, name):
    t = "mobile/member/teacher/" + name + ".html"
    return render(request, t, locals())
