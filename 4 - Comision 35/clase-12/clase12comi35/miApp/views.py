from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

estudiantes_inscriptos = [
        {"nombre" : "Juana", "cursos_realizados" : [
            {"titulo": "Django", "desc": "Framework de Python"},
            {"titulo": "CSS", "desc": "Bases del diseño web"},
            {"titulo": "Javascript", "desc": "Dinamismo en tu web"},
        ]},
        {"nombre" : "Carla", "cursos_realizados" : [
            {"titulo": "React", "desc": "Framework de JavaScript"}
        ]},
        {"nombre" : "Tito", "cursos_realizados" : [
            {"titulo": "CSS", "desc": "Bases del diseño web"},
            {"titulo": "Javascript", "desc": "Dinamismo en tu web"},
            {"titulo": "PHP", "desc": "Bases del diseño web"},
            {"titulo": "Laravel", "desc": "Dinamismo en tu web"},
            {"titulo": "Svetle", "desc": "Framework de JavaScript"}
        ]},
        {"nombre" : "Marcos", "cursos_realizados" : [
            {"titulo": "PHP", "desc": "Bases del diseño web"},
            {"titulo": "Laravel", "desc": "Dinamismo en tu web"},
            {"titulo": "Svetle", "desc": "Framework de JavaScript"}]},
        {"nombre" : "Laura", "cursos_realizados" : []},
        {"nombre" : "Pedro", "cursos_realizados" : [
            {"titulo": "PHP", "desc": "Bases del diseño web"},
            {"titulo": "Laravel", "desc": "Dinamismo en tu web"}
        ]}
    ]

# renderización de lista_estudiante 
def lista_estudiantes(request):
    doc_externo = open("C:/Users/Guido/Desktop/proyectosdjango/clase12comi35/miApp/templates/lista_estudiantes.html")
    template = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"estudiantes" : estudiantes_inscriptos})
    return HttpResponse(template.render(contexto))

# renderización de saludo
def saludo(request):
    
    doc_externo = open("C:/Users/Guido/Desktop/proyectosdjango/clase12comi35/miApp/templates/saludo.html")
    template = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"estudiantes" : estudiantes_inscriptos})
    return HttpResponse(template.render(contexto))

