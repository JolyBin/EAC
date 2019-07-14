from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


from .models import Entity
from .serializers import  Entity_Serializer


class Entity_View(generics.ListAPIView):

    queryset = Entity.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = Entity_Serializer

