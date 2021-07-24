from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# 注册：
class StudentAdmin(admin.ModelAdmin):
    # list_display这个属性即使用于定义文章列表页显示哪些字段，列表页中的值，必须和model类中声明的字段保持一致。
    list_display = ['studentname','studentid','Class','account']
    # 这个fields字段作用域model的添加页面，显示哪些字段可以用于输入内容，不在列表中的数据，默认添加页面就不在显示了。
    # fields = ['a_title']

    # fields属性和fieldsets属性不能同时使用。因为都作用于添加页面。
    #fieldsets = [
    #   ('标题信息', {'fields': ['n_title']}),
    #  ('作者信息', {'fields': ['n_author'], 'classes': ['collapse']}),
    #]

    # 针对文章列表页的一个属性配置，在列表页的右侧会出现一个过滤器，可以根据文章的发布时间或者作者对列表页的文章进行筛选。
    #list_filter = ['n_title', 'n_author']

    # 在文章的列表页顶部会出现一个搜索框。只能根据search_fields内部定义的字段值进行搜索。
    #search_fields = ['n_title', 'n_author']


admin.site.register(Student,StudentAdmin)
