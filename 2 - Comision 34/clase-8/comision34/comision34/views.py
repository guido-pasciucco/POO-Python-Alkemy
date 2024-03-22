from django.http import HttpResponse

def saludar(request):
    return HttpResponse("Hola mundo")

def despedida(request):
    return HttpResponse("Chauuuu")