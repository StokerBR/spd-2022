from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Usuário
    path('usuarios', views.user_index, name='user_index'),
    path('usuarios/criar', views.user_create, name='user_create'),
    path('usuarios/inserir', views.user_insert, name='user_insert'),
    path('usuarios/<int:id>/editar', views.user_edit, name='user_edit'),
    path('usuarios/atualizar', views.user_update, name='user_update'),
    path('usuarios/<int:id>/deletar', views.user_delete, name='user_delete'),

    # Alergias
    path('usuarios/<int:usuario_id>/alergias', views.allergy_index, name='allergy_index'),
    path('usuarios/<int:usuario_id>/alergias/criar', views.allergy_create, name='allergy_create'),
    path('usuarios/<int:usuario_id>/alergias/inserir', views.allergy_insert, name='allergy_insert'),
    path('usuarios/<int:usuario_id>/alergias/<int:id>/deletar', views.allergy_delete, name='allergy_delete'),

    # Vacinas
    path('vacinas', views.vaccine_index, name='vaccine_index'),
    path('vacinas/criar', views.vaccine_create, name='vaccine_create'),
    path('vacinas/inserir', views.vaccine_insert, name='vaccine_insert'),
    path('vacinas/<int:id>/editar', views.vaccine_edit, name='vaccine_edit'),
    path('vacinas/atualizar', views.vaccine_update, name='vaccine_update'),
    path('vacinas/<int:id>/deletar', views.vaccine_delete, name='vaccine_delete'),

    # Agendas
    path('agendas', views.schedule_index, name='schedule_index'),
    path('agendas/criar', views.schedule_create, name='schedule_create'),
    path('agendas/inserir', views.schedule_insert, name='schedule_insert'),
    path('agendas/<int:id>/realizar', views.schedule_perform, name='schedule_perform'),
    path('agendas/<int:id>/cancelar', views.schedule_cancel, name='schedule_cancel'),
    path('agendas/<int:id>/deletar', views.schedule_delete, name='schedule_delete'),

]
