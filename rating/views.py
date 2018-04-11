# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, HttpResponse
import data


# Create your views here.

def index(request):
    return render(request, 'rating/index.html')


def search(request, app_id):
    # print(app_id)
    datas = data.get_data(app_id, 1)
    return HttpResponse(datas)
    # return render(request, 'rating/index.html', {'app_id': app_id})
