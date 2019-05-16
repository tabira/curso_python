from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_cliente>', views.detalhe, name='detalhe'),
    path('<int:id_cliente>/lista', views.lista, name='lista'),
    path('<int:id_cliente>/confirma', views.confirma, name='confirma')

]
