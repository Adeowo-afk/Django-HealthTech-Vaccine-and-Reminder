from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import MedicationReminder
from .forms import ReminderForm

# --- CUSTOMER DASHBOARD (Read) ---
@login_required
def reminder_list(request):
    # Only show reminders belonging to the logged-in customer
    reminders = MedicationReminder.objects.filter(user=request.user)
    return render(request, 'reminders/reminder_list.html', {'reminders': reminders})

# --- CREATE REMINDER ---
@login_required
def reminder_create(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user  # Automatically attach the logged-in user
            reminder.save()
            return redirect('reminder_list')
    else:
        # Exclude 'user' from initial form input since we attach it automatically
        form = ReminderForm()
    
    return render(request, 'reminders/reminder_form.html', {'form': form, 'title': 'Add New Reminder'})

# --- UPDATE REMINDER ---
@login_required
def reminder_update(request, pk):
    reminder = get_object_or_404(MedicationReminder, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm(instance=reminder)
    
    return render(request, 'reminders/reminder_form.html', {'form': form, 'title': 'Edit Reminder'})

# --- DELETE REMINDER ---
@login_required
def reminder_delete(request, pk):
    reminder = get_object_or_404(MedicationReminder, pk=pk, user=request.user)
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminder_list')
    return render(request, 'reminders/reminder_confirm_delete.html', {'reminder': reminder})

# --- AUTHENTICATION VIEWS ---
def register_view(request):
    if request.user.is_authenticated:
        return redirect('reminder_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('reminder_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('reminder_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('reminder_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')






from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MedicationReminder
from .forms import ReminderForm

@login_required
def reminder_update(request, pk):
    reminder = get_object_or_404(MedicationReminder, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm(instance=reminder)
    
    return render(request, 'reminders/reminder_form.html', {'form': form, 'title': 'Edit Reminder'})