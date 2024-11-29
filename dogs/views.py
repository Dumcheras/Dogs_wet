from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from dogs.models import Category, Dog
from dogs.forms import DogForm


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


def category_dogs(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'category_dog_object_list': Dog.objects.all(category_id=pk),
        'title': f'Собаки породы - {category_item.name}',
        'category_pk': category_item.pk,
    }
    return render(request, 'dogs/dogs.html', context=context)


def dog_list_view(request):
    context = {
        'dog_object_list': Dog.objects.all(),
        'title': 'Все собаки'
    }
    return render(request, 'dogs/dogs.html', context=context)


def dog_create_view(request):
    if request.method == 'POST':
        form = DogForm(request.POST, request.FILES)
        if form.is_valid():
            dog_object = form.save()
            dog_object.save()
            return HttpResponseRedirect(reverse('dogs:dogs_list'))
    context = {
        'title': 'Добавить собаку',
        'form': DogForm(),
    }
    return render(request, 'dogs/create_update.html', context=context)


def dog_detail_view(request, pk):
    context = {
        'dog_object': Dog.objects.get(pk=pk),
        'title': 'Вы выбрали данного питомца'
    }
    return render(request, 'dogs/detail.html', context)
