from django.http import HttpResponse
from . import models


# Create your views here.

def index(request):
    ultimos_cinco = models.Adocao.objects.order_by('registro')[:5]

    retorno = ', '.join(str(adocao) for adocao in ultimos_cinco)

    return HttpResponse(retorno)


def detalhe_adocao(request, adocao_id):
    return HttpResponse('Under construction')


def clientes(request):
    return HttpResponse('Under construction')


def cliente_detalhe(request, cliente_id):
    return HttpResponse('Under construction')


def doadores(request):
    return HttpResponse('Under construction')


def doador_detalhe(request, doador_id):
    return HttpResponse('Under construction')


def animais(request):
    return HttpResponse('Under construction')


def animal_detalhe(request,animal_id):
    return HttpResponse('Under construction')


def racas(request):
    pass


def raca_detalhe(request, raca_id):
    pass
