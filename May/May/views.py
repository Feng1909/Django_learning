from django.shortcuts import render

def runoob(request):
  views_name = "菜鸟教程"
  return  render(request,"runoob.html", {"name":views_name})