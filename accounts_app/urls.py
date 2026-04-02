from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.users_list, name='users_list'),
    path('<username>/', views.profile, name='profile'),   
]  
