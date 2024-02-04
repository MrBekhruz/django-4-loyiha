from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name='home'),
    path('post-detail/<uuid:pk>/', post_detail,name='post_detail'),
    path('post-yaratish/', post_create,name='post_create'),
    path('<uuid:pk>/delete/', post_delete, name='delete'),
    path('<uuid:pk>/update/',post_update,name='post_tahrirlash')
]