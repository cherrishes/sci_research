# !/bash/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
__author__ = 'rdy'


def home(request):
    return render(request, "home.html", locals())

def member(request):
    return