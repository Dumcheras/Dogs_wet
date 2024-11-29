import random
import string

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm, UserPasswordChangeForm


def user_register_view(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password2'])
            new_user.save()
            return HttpResponseRedirect(reverse('users:user_login'))
    context = {
        'title': 'Регистрация пользователя',
        'form': form,
    }
    return render(request, 'users/user_register.html', context)


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(email=cleaned_data['email'], password=cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('dogs:index'))
                return HttpResponse('Аккаунт не активен')
        return HttpResponse('Аккаунт не создан')
    form = UserLoginForm()
    context = {
        'title': 'Вход в аккаунт',
        'form': form,
    }
    return render(request, 'users/user_login.html', context)


def user_profile_view(request):
    user_object = request.user
    context = {
        'title': f'Ваш профиль {user_object.first_name}',
    }
    return render(request, 'users/user_profile.html', context)
