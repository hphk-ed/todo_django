from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from .models import TodoList
from .serializers import TodoListSerializer


@api_view(['GET'])
def read(request):
    todolist = TodoList.objects.order_by('pk')

    serializer = TodoListSerializer(todolist, many=True)

    context = {
        'todos': serializer.data
    }
    return Response(context)

@api_view(['POST'])
def create(request):
    post_data = json.loads(request.body.decode('utf-8'))
    serializer = TodoListSerializer(data=post_data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    todolist = TodoList.objects.order_by('pk')
    todos = TodoListSerializer(todolist, many=True)
    context = {
        'todos': todos.data
    }
    return Response(context)


@api_view(['PUT', 'DELETE'])
def updatedelete(request, todo_pk):
    todo = get_object_or_404(TodoList, pk=todo_pk)  
    post_data = json.loads(request.body.decode('utf-8'))

    if request.method == "PUT":
        serializer = TodoListSerializer(data=post_data, instance=todo)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    elif request.method == "DELETE":
        todo.delete()
        
    todolist = TodoList.objects.order_by('pk')
    todos = TodoListSerializer(todolist, many=True)
    context = {
        'todos': todos.data
    }
    return Response(context)
