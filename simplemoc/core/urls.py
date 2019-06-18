from django.urls import include, re_path
from django.contrib import admin
from simplemoc.core import views

app_name='core'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^contato/$', views.contact, name='contact'),
]