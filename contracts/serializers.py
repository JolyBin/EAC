from rest_framework import serializers
from .models import Contarcts, Customers, Entity
from entity.serializers import Entity_Serializer


class Contracts_Serializer(serializers.ModelSerializer):
    """Сериализатор Контрактов."""

    custom = serializers.SerializerMethodField('_get_custom')
    offers = serializers.SerializerMethodField('_get_offer')

    @staticmethod
    def _get_custom(obj):
        """Получение всех детей модели Лицензии."""
        serializer = Customer_Serializer(
            obj.customer)
        return serializer.data

    @staticmethod
    def _get_offer(obj):
        """Получение всех детей модели Лицензии."""
        serializer = Entity_Serializer(
            obj.offer, many=True)
        return serializer.data

    class Meta:
        """Метакласс сериализатора."""

        model = Contarcts
        fields = ['number_contr', 'custom', 'txt_contacts', 'date_pub', 'offers', 'date_rec', 'sum_contr',
                  'close', 'cancel_contr', 'deadline', 'fine']


class Customer_Serializer(serializers.ModelSerializer):
    """Сериализатор владельца."""

    class Meta:
        """Метакласс сериализатора."""

        model = Customers
        fields = ['inn', 'ogrn', 'name_customer']


