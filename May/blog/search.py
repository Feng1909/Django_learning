from django.http import HttpResponse
from django.shortcuts import render
import requests
from . import views
import base64
import os


# 表单
def search_form(request):
    return render(request, 'search_form.html')

# 接收请求数据
def search(request):
    print("receivce")
    flag=0
    # request.encoding = 'utf-8'
    print("haha")
    print(request.FILES)
    #b64ImgData = request.FILES['image']
    try:
        studentname = request.FILES['stname']
    except KeyError:
        studentname=None
    try:
        stuid   = request.FILES['id']
    except KeyError:
        stuid= None
    try:
        stucla  = request.FILES['class']
    except KeyError:
        stucla  = None
        flag = 1
    try:
        stuacc  = request.FILES['account']
    except KeyError:
        stuacc = None
    try:
        stuimag = request.FILES['image']
    except KeyError:
        stuimag=None

    # print(filename.read())


    #with open(filename.read(), 'wb') as f:
    #    imgData = base64.b64decode(b64ImgData.read())
    #    f.write(imgData)

    # with open(filename, 'wb') as f:
    #     imgData = base64.b64decode(b64ImgData)
    #     f.write(imgData)

    #if 'q' in request.GET and request.GET['q']:
    #    message = '你搜索的内容为: ' + request.GET['q']
    #else:
    #    message = '你提交了空表单'
    #return HttpResponse(message)