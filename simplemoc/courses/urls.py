from django.urls import include, re_path
from django.contrib import admin
from simplemoc.courses import views

app_name='courses'

urlpatterns = [
    re_path(r'^$', views.courses, name = 'courses'),
    #re_path(r'^(?P<pk>\d+)/$', views.details, name = 'details'),
    re_path(r'^(?P<slug>[\w_-]+)/$', views.details, name = 'details'),
    re_path(r'^(?P<slug>[\w_-]+)/inscricao/$', views.enrollment, name = 'enrollment'),
    re_path(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$', views.undo_enrollment, name = 'undo_enrollment'),
    re_path(r'^(?P<slug>[\w_-]+)/anuncios/$', views.announcements, name = 'announcements'), 
]