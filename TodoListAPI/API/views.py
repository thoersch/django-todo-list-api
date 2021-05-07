from rest_framework import status, mixins, generics
from rest_framework.response import Response
from API.models import Todo
from API.serializers import TodoSerializer, IdsSerializer


class TodoList(mixins.DestroyModelMixin, generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def delete(self, request, *args, **kwargs):
        ids_serializer = IdsSerializer(data = request.data)
        ids_serializer.is_valid(raise_exception = True)
        ids = ids_serializer.data['ids']
        Todo.objects.filter(pk__in = ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer