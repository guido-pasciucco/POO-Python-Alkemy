from django.urls import path
from . import views

urlpatterns = [
    path('', views.test), # test.html (importa hijo.html)
    path('2', views.test2) # test_copy.html
]
