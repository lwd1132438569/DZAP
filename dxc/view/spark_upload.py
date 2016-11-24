#-*- coding: utf-8 -*-

from django.shortcuts import HttpResponse,render
from dxc.sparklib import spark_wordcount as wc

def spark_upload(request):
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
        res = wc.wordcount(myFile)
        return HttpResponse("Success!!!!! :" + str(res))
    return render(request, "spark_h5/spark_upload.html")