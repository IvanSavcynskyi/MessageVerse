from django.urls import path
from . import views

urlpatterns = [
    path('message/', views.send_message, name='send_message'),
    path('chat/<str:recipient_username>/', views.chat_detail, name='chat_detail'),
]