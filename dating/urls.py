from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.TestView, name='test'),
    path('message/', views.message, name='message'),
    path('contact/', views.contact, name='contact'),
    path('shortlist/', views.shortlist, name='shortlist'),
    path('shortlist-by/', views.shortlist_by, name='shortlist_by'),
    path('received/', views.received, name='received'),
    path('reject/', views.reject, name='reject'),
    path('viewed-myprofile/', views.viewed_myprofile, name='viewed_myprofile'),
    path('sent/', views.sent, name='sent'),
    path('accept/', views.accept, name='accept'),
]

              


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)