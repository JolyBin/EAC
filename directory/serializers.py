from rest_framework import serializers
from .models import City, Region, Country


class City_Serializer(serializers.ModelSerializer):
    """Сериализатор Негатива."""
    params = serializers.SerializerMethodField('param')

    @staticmethod
    def param(obj):
        import re

        text = re.sub(r'\([^()]*\)', '', obj.text.split(';'))
        return text.split(';')

    class Meta:
        model = City
        fields = ['id', 'params']



