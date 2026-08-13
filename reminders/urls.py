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


from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
]





from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('create/', views.reminder_create, name='reminder_create'),
    path('update/<int:pk>/', views.reminder_update, name='reminder_update'),
    path('delete/<int:pk>/', views.reminder_delete, name='reminder_delete'),
    
    # Auth
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]