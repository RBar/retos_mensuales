from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string  # cambiado
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


def index(request):
    lista_de_items = ""
    meses = list(nuestros_retos_mensuales.keys())
    for mes in meses:
        mes_en_mayuscula = mes.capitalize()
        ruta = reverse("retos-mensuales", args=[mes])
        lista_de_items += f"<li><a href =\"{ruta}\"> {mes_en_mayuscula} </a> </li>"
    respuesta = f"<ul>{lista_de_items}</ul>"
    return HttpResponse(respuesta)


def retos_mensuales_por_numero(request, mes):
    meses = list(nuestros_retos_mensuales.keys())
    if mes > len(meses):
        return HttpResponseNotFound("Este mes no es valido")
    mes_desde_numero = meses[mes-1]
    redirect_path = reverse("retos-mensuales", args=[mes_desde_numero])
    return HttpResponseRedirect(redirect_path)


def retos_mensuales(request, mes):
    try:
        reto = nuestros_retos_mensuales[mes]
        return render(request, "retos/retos.html")
        # respuesta = render_to_string("retos/retos.html")  # Cambiado
        # return HttpResponse(respuesta)
    except:
        return HttpResponseNotFound("Este mes no es valido")
