from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

# STRING {logica}
# F-STRING - CADENAS DE TEXTO EN LAS QUE INCRUSTAMOS VARIABLES
""" def saludo1(request):
    documento = 
        <html>
            <body>
                    <i>Hola mundo</i>
            </body>
        </html>
    
    return HttpResponse(documento) """


def saludo2(request):
    estudiantes_inscriptos = [
        {"nombre" : "Juan", "cursos_realizados" : [
            {
                "titulo": "Django",
                "desc": "Framework de Python",
                "img": "django-logo.png",
            },
            {
                "titulo": "CSS",
                "desc": "Bases del diseño web",
                "img": "css-logo.png" 
                },
            {
                "titulo": "Javascript",
                "desc": "Dinamismo en tu web",
                "img": "javascript-logo.png" 
            }
        ]},
        {"nombre" : "Carla", "cursos_realizados" : [
            {
                "titulo": "React",
                "desc": "Framework de JavaScript",
                "img": "react-logo.jpg" 
                }
        ]},
        {"nombre" : "Tito", "cursos_realizados" : [
        ]}
    ]
    ruta = "C:/Users/Guido/Desktop/proyectosdjango/clase12comi33/miApp/templates/saludo.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"estudiantes": estudiantes_inscriptos})
    return HttpResponse(plantilla.render(contexto))
