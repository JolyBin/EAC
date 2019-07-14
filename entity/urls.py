from django.urls import path
from .views import Entity_View

urlpatterns = [
    path('', Entity_View.as_view()),
]
