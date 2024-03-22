from django.template import Template, Context

# 1 - creación del objeto de tipo template
documento_ext = "ruta de ese documento (el html)"

plt = Template(documento_ext.read())

# 2 - creación del contexto - guarda el contenido dinámico 
# datos adicionales para el template (variables, funciones, etc)

ctx = Context()

# 3 - renderizar el objeto template

documento = plt.render(ctx)
#     renderuzi          plantilla        contexto
# return render(request, 'index.html', {{"nombre": nombre}})

