from retrocollector.models import Collectible
from rest_framework import serializers


class CollectibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collectible
        fields = ['name', 'type', 'date_manufactured', 'date_added', 'description']

