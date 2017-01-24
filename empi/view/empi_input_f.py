#-*- coding: utf-8 -*-

from django.shortcuts import render,HttpResponse
from empi.forms import Empi_input_f
from empi.empilib import empi_match_f

def empi_input(request):
    if request.method=="POST":  #这里POST一定要大写
        #通常获取请求信息
        name = request.POST.get("name",None)
        sex = request.POST.get("sex", None)
        addr = request.POST.get("addr", None)
        # patient_code = request.POST.get("patient_code", None)
        id_card = request.POST.get("id_card", None)
        # insure_id = request.POST.get("insure_id", None)
        birthday = request.POST.get("birthday", None)

        res = empi_match_f.match_id(name, sex, birthday, id_card, addr)

        #获取请求内容，做验证
        f = Empi_input_f(request.POST)  #request.POST：将接收到的数据通过Form1验证
        if f.is_valid():  #验证请求的内容和Form1里面的是否验证通过。通过是True，否则False。
            return render(request,"empi/empi_output.html",{'res':res})
            # print(f.cleaned_data)  #cleaned_data类型是字典，里面是提交成功后的信息
            # return HttpResponse(str(a))
            # return HttpResponse(str(b))
            #return HttpResponse("success! the result is:  "+ str(res))

        else:  #错误信息包含是否为空，或者符合正则表达式的规则
            print(type(f.errors),f.errors)  #errors类型是ErrorDict，里面是ul，li标签
            return render(request,"empi/empi_input_f.html",{"error":f.errors})
    return render(request,"empi/empi_input_f.html")


