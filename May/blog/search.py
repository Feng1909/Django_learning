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
    print(request.FILES)
    files = request.FILES

    #这里用来接收数据，如果函数不可行可以使用request.POST.get 或request.GET.get
    try:
        # stname = files.get('name',None)
        stname = request.POST.get('name', None)
        print("name:")
        print(stname)
    except KeyError:
        print("name error")
        stname=None
    try:
        # stuid   = files.get('id',None)
        stuid = request.POST.get('id', None)
        print("id")
        print(stuid)
        if(stuid == "-1"):
            flag = 1
    except KeyError:
        stuid= None
        print("id error")
        flag = 1    #用于判断人脸识别执行注册或是登录
    try:
        # stucla  = files.get('class',None)
        stucla = request.POST.get('class',None)
        print("class:")
        print(stucla)
    except KeyError:
        print("class error")
        stucla  = None

    try:
        # stuacc  = files.get('account',None)
        stuacc = request.POST.get('account', None)
    except KeyError:
        print("account error")
        stuacc = None
    try:
        content = files.get('image',None).read();        
        '''
        设置保存路径
            settings.IMAGES_DIR 已经默认设定
            默认保存文件名字为aaa.jpg
        '''
        with open("./reg.png",'wb') as f:
            f.write(content) 
    except KeyError:
        print("image error")
        stuimag=None

    #人脸识别
    if(flag==1):       #登录
        # print(os.system("pwd"))
        os.system('cd /root/lib-face-rec && ./libFaceRec /root/Django_learning/May/reg.png 2')
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

        os.system('cd /root/lib-face-rec && ./libFaceRec /root/Django_learning/May/reg.png 1 %s' %stuid)
        #新用户
        Student.objects.create(studentname=stname, studentid=stuid, Class=stucla, account=stuacc)
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