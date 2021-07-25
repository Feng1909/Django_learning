from django.http import HttpResponse
from django.http.response import FileResponse
from django.shortcuts import render
import requests
from .models import Student
import base64
import os
import qrcode

# 表单
def search_form(request):
    return render(request, 'search_form.html')

# 接收请求数据
def search(request):
    print("receive")
    flag=0
    # request.encoding = 'utf-8'
    #print("haha")
    print(request.FILES)
    #b64ImgData = request.FILES['image']

    #这里用来接收数据，如果函数不可行可以使用request.POST.get 或request.GET.get
    try:
        stname = request.FILES['name']
    except KeyError:
        stname=None
    try:
        stuid   = request.FILES['id']
    except KeyError:
        stuid= None
        flag = 1    #用于判断人脸识别执行注册或是登录
    try:
        stucla  = request.FILES['class']
    except KeyError:
        stucla  = None

    try:
        stuacc  = request.FILES['account']
    except KeyError:
        stuacc = None
    try:
        stuimag = request.FILES['image']
        stuimag.save('./reg.png')
    except KeyError:
        stuimag=None

    #人脸识别
    if(flag==1):       #登录
        print(os.system("pwd"))
        os.system('cd ... && cd lib-face-rec && ./libFaceRec ./reg.png 2')
        #这里有个读取文件识别结果的过程我不太知道格式~/result.txt
        with open("/root/result.txt", "r") as f:
            a = f.readlines()
        

        if(float(a[0][:-1]) >= 0.95):
            #如果成功
            print('人脸识别成功，返回账户信息')
            #生成二维码部分
            #QRImagePath = os.getcwd() + '/qrcode.png'   #临时存储位置
            qr = qrcode.QRCode(
                 version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=2,)   #设置图片格式
            qr.add_data(stuid)  #学号信息
            qr.make(fit=True)
            qrimg = qr.make_image()
            #img.save('qrcode.png')
            return HttpResponse(qrimg, content_type="image/png")   #返回一个二维码
        else:
            #身份验证失败
            message='人脸识别失败，请重新验证'
            print('人脸识别失败，请重新验证')
            return HttpResponse(message)


    elif(flag==0):     #注册

        os.system('cd ... && cd lib-face-rec && ./libFaceRec ./reg.png 1 %s' %stuid)
        #新用户
        Student.objects.create(studentname=stname, studentid=stuid, Class=stucla, account=stuacc, image=stuimag)
        message='识别成功，新用户已创建'
        return HttpResponse(message)

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