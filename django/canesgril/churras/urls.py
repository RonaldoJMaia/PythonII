from django.urls import path
from .views import index, churrasco, contato

urlpatterns = [
    path('', index),
    path('<int:id>', churrasco, name='churrasco'),
    path('contato', contato),
] 