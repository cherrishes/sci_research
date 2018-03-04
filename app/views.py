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
    return render(request, "member/teacher.html", locals())