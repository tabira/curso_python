from django.http import HttpResponse
from . import models
from django.shortcuts import render,get_object_or_404

# Create your views here.

def index(request):

    clientes = models.Cliente.objects.order_by('-registrado_em')[:5]

    #retorno =', '.join(cliente.nome for cliente in ultimos_cliente)
    context = { 'ultimos_clientes':clientes}

    return render(request,'reservas/index.html',context)


def detalhe(request, id_cliente):
    # try:
    #     cliente = models.Cliente.objects.get(id=id_cliente)
    # except models.Cliente.DoesNotExist:
    #     raise Http404()
    cliente = get_object_or_404(
        models.Cliente,
        id=id_cliente
    )

    return render(request,'reservas/detalhe.html',{'cliente':cliente})


def lista(reques, id_cliente):
    return HttpResponse(f'Lista do cliente - {id_cliente}')


def confirma(reques, id_cliente):
    return HttpResponse(f'Confirma do cliente - {id_cliente}')
