from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse

from .models import TodoList
from .serializers import TodoListSerializer

def alltodos(request):
    todolist = TodoList.objects.order_by('pk')

    todos = TodoListSerializer(todolist, many=True)
    
    context = {
        'todos': todos.data,
    }

    return JsonResponse(context)

def addtodo(request):

    # print(request.GET)
    todo = TodoListSerializer(data=request.GET)
    if todo.is_valid(raise_exception=True):
        res = todo.save()

    return redirect('todolists:all')


def update(request, todo_pk):
    todo = get_object_or_404(TodoList, pk=todo_pk)

    serializer = TodoListSerializer(data=request.GET, instance=todo)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        todo = get_object_or_404(TodoList, pk=todo_pk)
    
    return redirect('todolists:all')


def delete(request, todo_pk):
    todo = get_object_or_404(TodoList, pk=todo_pk)
    
    todo.delete()

    return redirect('todolists:all')
