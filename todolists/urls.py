from django.urls import path

from . import views

app_name = 'todolists'

urlpatterns = [
    path('', views.alltodos, name="all"),
    path('add/', views.addtodo, name="add"),
    path('update/<todo_pk>/', views.update, name="update"),
    path('delete/<todo_pk>/', views.delete, name="delete"),
]
