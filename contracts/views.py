from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


from .models import Contarcts
from .serializers import Contracts_Serializer


class Contracts_View(generics.ListAPIView):

    queryset = Contarcts.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = Contracts_Serializer
