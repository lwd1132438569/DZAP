#-*- coding: utf-8 -*-

from django.shortcuts import HttpResponse,render
from dxc.code import dxc_LinearRegression,dxc_NN
import os

def upload(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        # destination = open(os.path.join("D:\jg", myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        # for chunk in myFile.chunks():      # 分块写入文件
        #     destination.write(chunk)
        # destination.close()
        # res = dxc_LinearRegression.lr(myFile)
        # return HttpResponse("res success!:" + str(res))
        res = dxc_NN.nn(myFile)
        return HttpResponse("res success!:" + str(res))
    return render(request, "dxc/upload.html")