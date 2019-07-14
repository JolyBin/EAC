from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


from .models import Entity, Exec_Proc, Negative, Balance, Sum, Branch, Leader, Founders, Activity, License
from .serializers import Negative_Serializer, Branch_Serializer, Exec_Serializer, Sum_Serializer, Balance_Serializer, \
    Activity_Serializer, Founders_Serializer, License_Serializer, Entity_Serializer, Leader_Serializer


class Entity_View(generics.ListAPIView):

    queryset = Entity.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = Entity_Serializer

# Create your views here.
