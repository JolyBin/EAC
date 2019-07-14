from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('entity/', include('entity.urls')),
    path('contracts/', include('contracts.urls'))
]
