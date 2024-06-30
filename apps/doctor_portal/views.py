from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_portal/dashboard.html')

@login_required
def patient_list(request):
    # Placeholder for patient list logic
    return render(request, 'doctor_portal/patient_list.html')

@login_required
def appointments(request):
    # Placeholder for appointments logic
    return render(request, 'doctor_portal/appointments.html')

@login_required
def consultation_notes(request):
    # Placeholder for consultation notes logic
    return render(request, 'doctor_portal/consultation_notes.html')