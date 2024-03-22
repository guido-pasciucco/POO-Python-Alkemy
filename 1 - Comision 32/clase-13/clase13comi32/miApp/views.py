from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse


def test(request):
    ruta = "C:/Users/Guido/Desktop/proyectosdjango/clase13comi32/miApp/templates/test.html"
    doc_ext = open(ruta)
    template = Template(doc_ext.read())
    doc_ext.close()
    contexto = Context()
    return HttpResponse(template.render(contexto))

def test2(request):
    ruta = "C:/Users/Guido/Desktop/proyectosdjango/clase13comi32/miApp/templates/test_copy.html"
    doc_ext = open(ruta)
    template = Template(doc_ext.read())
    doc_ext.close()
    contexto = Context()
    return HttpResponse(template.render(contexto))
