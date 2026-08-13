from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('create/', views.reminder_create, name='reminder_create'),
    path('update/<int:pk>/', views.reminder_update, name='reminder_update'),
    path('delete/<int:pk>/', views.reminder_delete, name='reminder_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('add/', views.reminder_create, name='reminder_create'),
    path('delete/<int:pk>/', views.reminder_delete, name='reminder_delete'),
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



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'reminders/register.html', {'form': form})