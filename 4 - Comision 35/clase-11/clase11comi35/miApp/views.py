from django.shortcuts import render

# Create your views here.
def ejemplo(request):
    nombre = "Pepito"
    return render(request, 'test.html', {'nombreUsuario': nombre})