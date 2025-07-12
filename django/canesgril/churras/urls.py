from django.urls import path
from .views import index, churrasco, contato, buscar

urlpatterns = [
    path('', index, name='index'),
    path('buscar/', buscar, name='buscar'),
    path('<int:id>', churrasco, name='churrasco'),
    path('contato', contato),
] 