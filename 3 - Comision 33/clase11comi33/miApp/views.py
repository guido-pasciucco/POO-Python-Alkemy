from django.shortcuts import render

# Create your views here.
def saludo(request):
    nombre_usuario = "Camila"
    return render(
        request,
        'test.html',
        {'nombre_usuario': nombre_usuario}
    )