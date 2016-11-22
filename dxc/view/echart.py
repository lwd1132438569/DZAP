#-*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render

def bar(request):
    if request.method == "POST":
        name_dict = {'衬衫': '5', '羊毛衫': '2', '雪纺衫': '36', '裤子': '10', '高跟鞋': '10', '袜子': '20'}
        return JsonResponse(name_dict)
    return render(request,"echart/bar.html")

def bar_static(request):
    return render(request,"echart/bar_static.html")