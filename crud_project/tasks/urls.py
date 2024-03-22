from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'), # task list
    path('task/<int:task_id>/', views.task_detail, name='task_detail'), # detalle de la tarea
    path('task/create/', views.task_create, name='task_create'), # crear nueva tarea
    path('task/<int:task_id>/update/', views.task_update, name='task_update'), # actualizar x tarea
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'), # borrar x tarea
]