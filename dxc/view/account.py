#-*- coding: utf-8 -*-

from django.shortcuts import render,HttpResponse
from dxc.forms import Form1

def form1(request):
    if request.method=="POST":  #这里POST一定要大写
        #通常获取请求信息
        a = request.POST.get("user",None)
        b = request.POST.get("pwd",None)
        #获取请求内容，做验证
        f = Form1(request.POST)  #request.POST：将接收到的数据通过Form1验证
        if f.is_valid():  #验证请求的内容和Form1里面的是否验证通过。通过是True，否则False。
            # print(f.cleaned_data)  #cleaned_data类型是字典，里面是提交成功后的信息
            # return HttpResponse(str(a))
            # return HttpResponse(str(b))
            return HttpResponse(str(f))
        else:  #错误信息包含是否为空，或者符合正则表达式的规则
            print(type(f.errors),f.errors)  #errors类型是ErrorDict，里面是ul，li标签
            return render(request,"account/form1.html",{"error":f.errors})
    return render(request,"account/form1.html")