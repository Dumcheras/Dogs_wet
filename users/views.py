import random
import string

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm, UserPasswordChangeForm
ljfrom users.services import send_new_password, send_register_email


def user_register_view(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password2'])
            new_user.save()
            send_register_email(new_user.email)
            print('Письмо о регистрации отправлено!')
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


def user_update_view(request):
    user_object = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user_object)
        if form.is_valid():
            user_object = form.save()
            user_object.save()
            return HttpResponseRedirect(reverse('users:user_profile'))
    user_name = user_object.first_name
    context = {
        'title': f'Изменить профиль {user_name}',
        'user_object': user_object,
        'form': UserUpdateForm(instance=user_object)
    }
    return render(request, 'users/user_update.html', context)


def user_change_password_view(request):
    user_object = request.user
    form = UserPasswordChangeForm(user_object, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user_object = form.save()
            update_session_auth_hash(request, user_object)
            messages.success(request, 'Пароль успешно изменен')
            return HttpResponseRedirect(reverse('users:user_profile'))
        messages.error(request, 'Не удалось изменить пароль')
    context = {
        'title': 'Изменить пароль',
        'form': form,
    }
    return render(request, 'users/user_change_password.html', context)


def user_logout_view(request):
    logout(request)
    return redirect('dogs:index')


def user_generate_new_password(request):
    new_password = ''.join(random.sample((string.ascii_letters + string.digits), 12))
    request.user.set_password(new_password)
    request.user.save()
    send_new_password(request.user.email, new_password)
    return redirect(reverse('dogs:index'))
