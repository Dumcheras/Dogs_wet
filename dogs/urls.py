from django.urls import path
from dogs.views import index, categories
from dogs.apps import DogsConfig

app_name = DogsConfig.name

#пути к страницам на сайте
urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
]