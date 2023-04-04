from django.urls import path, include
from .views import *

urlpatterns = [
    path('movie/', movie_list),
    path('movie/<int:pk>/', movie_detail)
]