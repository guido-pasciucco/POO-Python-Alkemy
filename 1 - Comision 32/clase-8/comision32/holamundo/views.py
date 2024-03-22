from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo")

def despedida(request):
    return HttpResponse("Hasta pronto")