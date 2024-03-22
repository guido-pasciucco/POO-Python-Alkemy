from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context



# una lista de diccionarios


def saludar(request):
    
    cursos_realizados = [
        {"titulo": "HTML y CSS", "descripcion": "Bases para el maquetado web"},
        {"titulo": "Javascript", "descripcion": "Esencial para una web dinámica"},
        {"titulo": "React", "descripcion": "Tu app web al siguiente nivel"},
        {"titulo": "SQL", "descripcion": "Tu primer base de datos"},
    ]

    # establezco un archivo externo (la plantilla) y paso la ruta, para abrirla
    doc_externo = open("C:/Users/Guido/Desktop/proyectosdjango/clase12comi34/miApp/templates/saludo.html")
    
    # establecemos un dato que queremos mostrar en el template
    nombre = "Pedro"

    # establecemos una variable plantilla, que es una inicialización del objeto
    # TEMPLATE (PLANTILLA), que toma como parámetro, la lectura del doc. externo)
    plantilla = Template(doc_externo.read())
    
    # CERRAMOE EL DOC EXTERNO para evitar perdida de performance
    doc_externo.close()

    # creamos el contexto, en este caso, está vacío 
    contexto = Context({"nombre_usuario": nombre, "cursos" : cursos_realizados})

    # RENDERIZAMOS LA PLANTILLA, TENIENDO EN CUENTA EL CONTEXTO
    return HttpResponse(plantilla.render(contexto))
