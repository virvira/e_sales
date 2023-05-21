from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('network_items/', include('network_items.urls')),
    path('core/', include('core.urls')),
]
