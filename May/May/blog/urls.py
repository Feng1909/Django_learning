#booktest/urls.py
from django.conf.urls import url
from . import views
from . import search
from django.contrib import admin
urlpatterns=[
    url(r'^index/$',views.index),
    #url(r'^(\d+)$',views.show),
    url(r'^new/$',views.NewUser),
    url(r'^delete/$',views.DeleteUser),
    url(r'^modify/$',views.Modification),
    url(r'^admin/',admin.site.urls),
    url(r'^haha/', search.search),
]