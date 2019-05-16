from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:adocao_id>/', views.detalhe_adocao, name='detalhe'),
    path('clientes/', views.clientes, name='lista'),
    path('clientes/<int:cliente_id>/', views.cliente_detalhe,name='cliente_detalhe'),
    path('doadores/', views.doadores, name='doadores'),
    path('doadores/<int:doador_id>/', views.doador_detalhe,name='doador_detalhe'),
    path('animais/', views.animais, name='animais'),
    path('animais/<int:animal_id>/', views.animal_detalhe,name='animal_detalhe'),
    path('racas/', views.racas, name='racas'),
    path('racas/<int:raca_id>/', views.raca_detalhe ,name='raca_detalhe')


]
