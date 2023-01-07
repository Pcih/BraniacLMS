"""Конфигурация URL-адреса конфигурации конфигурации

Список `urlpatterns` направляет URL-адреса к представлениям. Для получения дополнительной информации, пожалуйста, смотрите:
https://docs.djangoproject.com/en/3.2/topics/http/urls/
Примеры:
Функциональные представления
1. Добавьте импорт: из представлений импорта my_app
2. Добавьте URL-адрес в urlpatterns: path(", views.home, name='home')
Представления на основе классов
1. Добавьте импорт: из other_app.views импортировать домой
2. Добавьте URL-адрес в urlpatterns: path(", Home.as_view(), name='home')
Включая другой URLconf
1. Импортируйте функцию include(): из django.urls импортируйте include, путь
2. Добавьте URL в urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="mainapp/")),
    path("mainapp/", include("mainapp.urls")),
]
