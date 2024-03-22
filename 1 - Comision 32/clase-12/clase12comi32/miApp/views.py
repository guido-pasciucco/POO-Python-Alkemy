from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
import datetime

# Create your views here.

def saludo1(request):
    documento = """
        <html>
            <body>
                <h1>
                    Hola mundoooo
                </h1>
            </body>
        </html>
    """
    return HttpResponse(documento)



def saludo2(request):
    # open , read, close, render
    # preparamos el terreno para (quizás, o no) unir logica con presentación
    # llamo a ese doc en una variable
    ruta = "C:/Users/Guido/Desktop/proyectosdjango/clase12comi32/miApp/templates/plantilla1.html"
    doc_externo = open(ruta)
    # creo el objeto template donde leo el doc externo
    plantilla = Template(doc_externo.read())
    # cerrarlo para no consumir recursos de más
    doc_externo.close()
    # lugar donde se almacenan la lógica que se va a usar / mostrar en la plantilla
    # creamos un contexto, en este caso vacío
    contexto = Context()
    # renderizar el doc
    # renderizo la plantilla, pasándole los datos que hay en el contexto
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

# utilizar variables y referenciar valores en la plantilla, desde el view

def saludo3(request):
    nombre = "Pedro"
    fecha_actual = datetime.datetime.now()
    cursos = [ {"curso": "React",  "descripcion" : "Framework de JS" },
        {"curso": "Django", "descripcion" : "Framework de Pythoh"},
        {"curso":  "PHP", "descripcion" : "Uno de los lenguajes más populares" },
        {"curso":  "Javascript", "descripcion" : "Ideal para Web"  },
        {"curso":  "Laravel",  "descripcion" : "Lorem ipsum" },
        {"curso": "Java",  "descripcion" : "Ideal para POO"},
        {"curso": "Angular", "descripcion" : "Framework de JS" },
        {"curso":  "Golang", "descripcion" : "Lorem Ipsum" },
    ]
    ruta = "C:/Users/Guido/Desktop/proyectosdjango/clase12comi32/miApp/templates/plantilla3.html" 
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({
        "nombre_user": nombre,
        "fecha_actual" : fecha_actual,
        "cursos" : cursos
    })
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

# llamar a métodos desde las platillas
# jerarquia / orden en llamadas desde plantillas
# uso de listas en contexto y plantillas
# estructura de control de flujo en plantillas
