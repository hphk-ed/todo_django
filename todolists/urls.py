from django.urls import path

from . import views

app_name = 'todolists'

urlpatterns = [
    path('', views.read, name="r"),
    path('todo/', views.create, name='c'),
    path('todo/<todo_pk>/', views.updatedelete, name="ud"),
]
