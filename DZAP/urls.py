"""DZAP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from dxc.view import account,dxc_input,upload,echart,spark_upload
from empi.view import empi_input,empi_input_jb,empi_input_f

urlpatterns = [
    url(r'^dxc/', include('dxc.urls')),
    url(r'^form1/', account.form1),
    url(r'^dxc_input/',dxc_input.dxc_input),
    url(r'^upload/',upload.upload),
    url(r'^echart/',echart.bar_static),
    url(r'^echart_1/',echart.bar),
    url(r'^spark_upload/',spark_upload.spark_upload),
    url(r'^empi_input/',empi_input.empi_input),
    url(r'^empi_input_jb/',empi_input_jb.empi_input),
    url(r'^empi_input_f/',empi_input_f.empi_input),
    url(r'^admin/', admin.site.urls),
]


