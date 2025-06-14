from django.urls import path
from .views import index, churrasco, contato
urlpatterns = [
    path('', index),
    path('churrasco', churrasco),
    path('contato', contato),
]