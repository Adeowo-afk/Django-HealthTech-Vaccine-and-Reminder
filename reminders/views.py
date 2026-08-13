from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MedicationReminder

@login_required
def reminder_list(request):
    reminders = MedicationReminder.objects.filter(user=request.user)
    return render(request, 'reminders/reminder_list.html', {'reminders': reminders})


@login_required
def reminder_create(request):
    if request.method == 'POST':
        MedicationReminder.objects.create(
            user=request.user,
            medication_name=request.POST['medication_name'],
            dosage=request.POST['dosage'],
            scheduled_time=request.POST['scheduled_time'],
            reminder_time=request.POST['reminder_time'],
            notification_type=request.POST['notification_type'],
            phone_number=request.POST.get('phone_number', ''),
        )
        return redirect('reminder_list')
    return render(request, 'reminders/reminder_form.html')


@login_required
def delete_reminder(request, pk):
    reminder = get_object_or_404(MedicationReminder, pk=pk, user=request.user)
    reminder.delete()
    return redirect('reminder_list')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MedicationReminder  # or your reminder model name
from .forms import ReminderForm         # form for creating reminders

@login_required
def reminder_list(request):
    # Fetch reminders belonging to the logged-in user
    reminders = MedicationReminder.objects.filter(user=request.user)
    return render(request, 'reminders/dashboard.html', {'reminders': reminders})
