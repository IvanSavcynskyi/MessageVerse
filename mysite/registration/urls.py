from . import views
from django.urls import path, include

urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('login/', views.login_view, name='login'),
]