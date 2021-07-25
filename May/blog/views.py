from django.shortcuts import render
from .models import Student
# Create your views here.
from django.http import HttpResponse
from . import search
def DeleteUser(request):
    s = Student.objects.filter(studentname='朱胤儒')
    s.delete()
    return render(request,'DeleteUser.html', locals())

def NewUser(request):
    postname='黄启辰'
    postid='1120190721'
    #这种方法容易重复写入
    #studentname=request.POST.get('postname')
    #studentid=request.POST.get('postid')
    #s = Student()
    #s.studentid=studentname
    #s.studentid=studentid
    #s.save()
    Student.objects.create(studentname=postname,studentid=postid)
    return render(request,'NewUser.html', locals())

def Modification(request):
    formalpostname='黄启辰'
    formalpostid='1120190721'
    s = Student.objects.get(studentname=formalpostname)
    s.studentname='朱胤儒'
    s.studentid='1120190726'
    s.save()
    return HttpResponse("success")
def index(request):
    namelist = Student.objects.all()
    return render(request,'index.html', locals())

    #return HttpResponse("index.html")

