from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from dogs.models import Category, Dog


# делаем страницы сайта
def index(request):
    context = {
        'category_object_list': Category.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context=context)


def categories(request):
    context = {
        'category_object_list': Category.objects.all(),
        'title': 'Питомник - Все породы'
    }
    return render(request, 'dogs/categories.html', context=context)
