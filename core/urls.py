from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name='home'),
    path('post-detail/<uuid:pk>/', post_detail,name='post_detail'),
    path('post-yaratish/', post_create)
]