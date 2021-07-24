from django.conf.urls import include,url
# from . import views, search2
from ..blog import views
from ..blog import search
from django.contrib import admin
import sys,os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')


urlpatterns = [
    url(r'^index/$',views.index),
    #url(r'^(\d+)$',views.show),
    url(r'^new/$',views.NewUser),
    url(r'^delete/$',views.DeleteUser),
    url(r'^modify/$',views.Modification),
    url(r'^admin/',admin.site.urls),
    url(r'^', search.search),

]
'''
from django.conf.urls import url
from . import views
from . import search
from django.contrib import admin

    url(r'^index/$',views.index),
    #url(r'^(\d+)$',views.show),
    url(r'^new/$',views.NewUser),
    url(r'^delete/$',views.DeleteUser),
    url(r'^modify/$',views.Modification),
    url(r'^admin/',admin.site.urls),
    url(r'^search/$', search.search),
'''