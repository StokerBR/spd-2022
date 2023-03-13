from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criar', views.create, name='create'),
    path('inserir', views.insert, name='insert'),
    path('<int:codigo>/editar', views.edit, name='edit'),
    path('atualizar', views.update, name='update'),
    path('<int:codigo>/deletar', views.delete, name='delete'),
]