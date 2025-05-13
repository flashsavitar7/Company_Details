from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_company, name='create_company'),
    path('success/', views.success_page, name='success'),
]
