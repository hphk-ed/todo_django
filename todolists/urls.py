from django.urls import path

from . import views

app_name = 'todolists'

urlpatterns = [
    path('', views.read, name="read"),
    path('<todo_pk>/', views.cud, name="cud"),
]
