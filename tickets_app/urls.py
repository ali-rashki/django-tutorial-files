from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add_ticket),
    path('list', views.show_all_tickets),
]