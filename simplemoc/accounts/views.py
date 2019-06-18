from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm,
    SetPasswordForm)
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

from simplemoc.core.utils import generate_hash_key
from simplemoc.courses.models import Enrollment

from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset

User = get_user_model()

@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    context = {}
    return render(request, template_name)

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

def password_reset(request):
    template_name = 'accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(request, template_name, context)

@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Os dados da sua conta foram alterados com sucesso')
            return redirect('accounts:dashboard') 
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
# from django.conf import settings
# from .forms import RegisterForm, EditAccountForm
# from django.contrib.auth import authenticate, login, get_user_model
# from django.contrib.auth.decorators import login_required
# from .models import PasswordReset
# from simplemoc.core.utils import generate_hash_key

# User = get_user_model()

# # Create your views here.

# @login_required
# def dashboard(request):
#     template_name = 'accounts/dashboard.html'
#     return render(request, template_name)

# def register(request):
#     template_name =  'accounts/register.html'
#     if request.method == 'POST':
#         #form = RegisterForm(request.POST)
#         if form.is_valid():
#             #user = form.save()
#             # user = authenticate(
#             #     username = user.username, password = form.cleaned_data['password1']
#             # )
#             # login(request,user)
#             return redirect('core:home')
#     else:
#         form = RegisterForm()
#     context = {
#         'form': form
#     }
#     return render(request, template_name, context)

# def password_reset(request):
#     template_name =  'accounts/password_reset.html'
#     context = {}
#     form = PasswordResetForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         context['sucess'] = True
#     context['form'] = form
#     return render(request, template_name, context)

# @login_required
# def edit(request):
#     template_name = 'accounts/edit.html'
#     context = {}
#     if request.method == 'POST':
#         form = EditAccountForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             form = EditAccountForm(instance=request.user)
#             context['sucess'] = True
#     else:
#         form = EditAccountForm(instance=request.user)
#     context['form'] = form
#     return render(request, template_name, context)

# @login_required
# def edit_password(request):
#     template_name = 'accounts/edit_password.html'
#     context = {}
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             context['success'] = True
#     else:
#         form = PasswordChangeForm(user=request.user)
#     context['form'] = form
#     return render(request, template_name, context)
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
# from django.conf import settings
# from .forms import RegisterForm, EditAccountForm
# from django.contrib.auth import authenticate, login, get_user_model
# from django.contrib.auth.decorators import login_required
# from .models import PasswordReset
# from simplemoc.core.utils import generate_hash_key

# # Create your views here.

# User = get_user_model()

# def register(request):
#     template_name =  'accounts/register.html'
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user = authenticate(
#                 username = user.username, password = form.cleaned_data['password1']
#             )
#             login(request,user)
#             return redirect('core:home')
#     else:
#         form = RegisterForm()
#     context = {
#         'form': form
#     }
#     return render(request, template_name, context)

# @login_required
# def dashboard(request):
#     template_name = 'accounts/dashboard.html'
#     return render(request, template_name)

# def password_reset(request):
#     template_name =  'accounts/password_reset.html'
#     form = PasswordResetForm(request.POST or None)
#     context = {}
#     if form.is_valid():
#         user = User.objects.get(email=form.cleaned_data['email'])
#         key = generate_hash_key(user.username)
#         reset = PasswordReset(key=key, user=user)
#         reset.save()
#         context['sucess'] = True
#     context['form'] = form
#     return render(request, template_name,context)

# @login_required
# def edit(request):
#     template_name = 'accounts/edit.html'
#     context = {}
#     if request.method == 'POST':
#         form = EditAccountForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             form = EditAccountForm(instance=request.user)
#             context['sucess'] = True
#     else:
#         form = EditAccountForm(instance=request.user)
#     context['form'] = form
#     return render(request, template_name, context)

# @login_required
# def edit_password(request):
#     template_name = 'accounts/edit_password.html'
#     context = {}
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             context['success'] = True
#     else:
#         form = PasswordChangeForm(user=request.user)
#     context['form'] = form
#     return render(request, template_name, context)