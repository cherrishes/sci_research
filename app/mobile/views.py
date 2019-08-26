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