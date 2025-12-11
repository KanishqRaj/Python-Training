from django.urls import path
from .views import hello,welcome

urlpatterns = [
    path('hello/', hello) , path('welcome/',welcome)
]
