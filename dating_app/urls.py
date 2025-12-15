from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dating/', include('dating.urls')),
    path('job/', include('jobPortal.urls')),
    path('matrimony/', include('matrimony.urls')),
]