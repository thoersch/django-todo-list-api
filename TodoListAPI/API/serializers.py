from rest_framework import serializers
from API.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'done', 'created']
        extra_kwargs = {'title': {'required': True}, 'done': {'required': True}}

class IdsSerializer(serializers.Serializer):
    ids = serializers.ListField(child = serializers.IntegerField())