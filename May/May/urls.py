from blog import search
from May import blog
from django.conf.urls import include,url
from blog import views
from django.contrib import admin

urlpatterns = [
    url(r'^hello/$', views.runoob),
    #url(r'^search-form/$', search.search_form),
    # url(r'^search-post/$', search2.search_post),
    # url(r'^',include('blog.urls')),
    url(r'^', search.search),
    url(r'^index/$',views.index),
    #url(r'^(\d+)$',views.show),
    url(r'^new/$',views.NewUser),
    url(r'^delete/$',views.DeleteUser),
    url(r'^modify/$',views.Modification),
    url(r'^admin/',admin.site.urls),

]