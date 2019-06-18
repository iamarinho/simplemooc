from django.urls import include, re_path
from django.contrib.auth import views
from simplemoc.accounts import views as views_accounts

app_name='accounts'

urlpatterns = [
    re_path(r'^/$', views_accounts.dashboard, name='dashboard'),    
    re_path(r'^entrar/$', views.LoginView.as_view(template_name ='accounts/login.html'), name='login'),    
    re_path(r'^cadastre-se/$', views_accounts.register, name='register'),  
    re_path(r'^nova-senha/$', views_accounts.password_reset, name='password_reset'),  
    re_path(r'^confirmar-nova-senha/(?P<key>\w+)$', views_accounts.password_reset_confirm, name='password_reset_confirm'), 
    re_path(r'^sair/$', views.LogoutView.as_view(next_page = 'core:home'), name='logout'),    
    re_path(r'^editar/$', views_accounts.edit, name='edit'),  
    re_path(r'^editar-senha/$', views_accounts.edit_password, name='edit_password'),  
]