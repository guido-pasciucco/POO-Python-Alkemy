from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

def mostrarTemplate(request):
    condicion = False
    ruta = "C:/Users/Guido/Desktop/proyectosdjango/clase13comi34/miApp/templates/index.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"condicion": condicion})
    return HttpResponse(plantilla.render(contexto))


def mostrarOtro(request):
    ruta = "C:/Users/Guido/Desktop/proyectosdjango/clase13comi34/miApp/templates/otro.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context()
    return HttpResponse(plantilla.render(contexto))