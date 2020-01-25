from rest_framework import serializers
from .models import Funhouse

class FunhouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funhouse
        fields = ('id', 'title', 'description', 'completed')
