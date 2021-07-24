# from May.blog import search
from May import blog
from django.conf.urls import include,url
from . import views, search2
#from ..blog import search
# from ..blog import search
from blog import search

urlpatterns = [
    url(r'^hello/$', views.runoob),
    #url(r'^search-form/$', search.search_form),
    url(r'^search-post/$', search2.search_post),
    # url(r'^',include('blog.urls')),
    url(r'^', search.search),

]