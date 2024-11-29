from django.urls import path
from dogs.views import index, categories, category_dogs, dog_list_view,dog_create_view,dog_detail_view
from dogs.apps import DogsConfig

app_name = DogsConfig.name

# пути к страницам на сайте
urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('categories/<int:pk>/dogs/', category_dogs, name='category_dogs'),
    path('dogs/', dog_list_view, name='dogs_list'),
    path('dogs/create/', dog_create_view, name='dog_create'),
    path('dogs/detail/<int:pk>/', dog_detail_view, name='dog_detail'),


]
