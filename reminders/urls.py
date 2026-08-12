from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('create/', views.reminder_create, name='reminder_create'),
    path('delete/<int:pk>/', views.delete_reminder, name='delete_reminder'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('add/', views.reminder_create, name='reminder_create'),
    path('delete/<int:pk>/', views.delete_reminder, name='delete_reminder'),
]