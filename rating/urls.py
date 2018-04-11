from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    # url(r'^search/', views.search, name='search'),
    url(r'^search/(?P<app_id>[0-9]+)/$', views.search, name='search'),
]
