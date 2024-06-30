from django.contrib import admin
from .models import Appointment, ConsultationNote

admin.site.register(Appointment)
admin.site.register(ConsultationNote)