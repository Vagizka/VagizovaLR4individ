#Маршруты URL для приложения tasks (модуль аудита).
#Связывает URL-адреса с функциями-представлениями.
from django.urls import path
from . import views  # Импортирую представления из текущего приложения

urlpatterns = [
    # Путь '' (корневой адрес) вызывает функцию views.index
    # name='index' - позволяет ссылаться на этот маршрут по имени
    path('', views.index, name='index'),
]