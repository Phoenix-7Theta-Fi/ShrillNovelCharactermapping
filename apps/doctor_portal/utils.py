from datetime import timedelta
from .models import Appointment

def get_available_slots(doctor, date):
    start_time = date.replace(hour=9, minute=0, second=0, microsecond=0)
    end_time = date.replace(hour=17, minute=0, second=0, microsecond=0)

    booked_slots = Appointment.objects.filter(
        doctor=doctor,
        appointment_date__date=date,
        status='scheduled'
    ).values_list('appointment_date', flat=True)

    available_slots = []
    current_slot = start_time
    while current_slot < end_time:
        if current_slot not in booked_slots:
            available_slots.append(current_slot)
        current_slot += timedelta(minutes=30)

    return available_slots

def is_slot_available(doctor, appointment_datetime):
    existing_appointment = Appointment.objects.filter(
        doctor=doctor,
        appointment_date=appointment_datetime,
        status='scheduled'
    ).exists()
    return not existing_appointment