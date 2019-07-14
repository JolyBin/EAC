from django.urls import path


from .views import Contracts_View

urlpatterns = [
    path('', Contracts_View.as_view()),
]
