from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


nuestros_retos_mensuales = {
    "enero": "Reto #1",
    "febrero": "Reto #2",
    "marzo": "Reto #3",
    "abril": "Reto #4",
    "mayo": "Reto #5",
    "junio": "Reto #6",
    "julio": "Reto #7",
    "agosto": "Reto #8",
    "septiembre": "Reto #9",
    "octubre": "Reto #10",
    "noviembre": "Reto #11",
    "diciembre": "Reto #12",
}


def retos_mensuales_por_numero(request, mes):
    reto = "Reto #" + str(mes)
    return HttpResponse(reto)


def retos_mensuales(request, mes):
    try:
        reto = nuestros_retos_mensuales[mes]
        return HttpResponse(reto)
    except:
        return HttpResponse("Este mes no es valido")
