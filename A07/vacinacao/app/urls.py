from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buscar', views.search, name='search'),
    path('criar', views.create, name='create'),
    path('inserir', views.insert, name='insert'),
    path('<int:id>/editar', views.edit, name='edit'),
    path('atualizar', views.update, name='update'),
    path('<int:id>/deletar', views.delete, name='delete'),
]