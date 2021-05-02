from retrocollector.models import Collectible, Type
from rest_framework import serializers


class CollectibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collectible
        fields = ['name', 'type', 'date_manufactured', 'date_added', 'description']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields =['name']
