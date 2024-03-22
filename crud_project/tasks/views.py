from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# CRUD (CREATE, READ, UPDATE, DELETE)

# READ
def task_list(request):
    tasks = Task.objects.all()
    #                       RUTA ................... CONTEXTO
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

# CREATE
def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(
            title = title,
            description = description
        )
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')

# UPDATE
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task.title = title
        task.description = description
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'task': task})

# DELETE
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

