from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from API.models import Todo
from API.serializers import TodoSerializer


class TodoList(APIView):
    """
    List or create todos
    """
    def get(self, request, format = None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    """
    CRUD on a todo
    """
    def get_object(self, pk):
        try:
            todo = Todo.objects.get(pk = pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)