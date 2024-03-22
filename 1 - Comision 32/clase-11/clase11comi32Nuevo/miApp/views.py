from django.shortcuts import render

def ejemplo_plantilla(request):
    nombre_usuario = {"nombre" : "Juan", "apellido" : "Perez"}
    return render(
        request,
        'mi_plantilla.html',
        {'nombre_usuario': nombre_usuario}
    )