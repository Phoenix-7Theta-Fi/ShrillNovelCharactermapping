from django.db import models
from apps.accounts.models import User

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class ConsultationNote(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)