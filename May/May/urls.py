from django.conf.urls import url
from . import views, search, search2

urlpatterns = [
    url(r'^hello/$', views.runoob),
    url(r'^search-form/$', search.search_form),
    url(r'^search-post/$', search2.search_post),
    url(r'^search/$', search.search),
]