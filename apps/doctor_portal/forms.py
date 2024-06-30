from django import forms
from .models import Appointment, ConsultationNote

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'appointment_date', 'status']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ConsultationNoteForm(forms.ModelForm):
    class Meta:
        model = ConsultationNote
        fields = ['notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
        }