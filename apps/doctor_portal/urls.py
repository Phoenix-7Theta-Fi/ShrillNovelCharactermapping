from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient-list/', views.patient_list, name='patient_list'),
    path('appointments/', views.appointments, name='appointments'),
    path('consultation-notes/', views.consultation_notes, name='consultation_notes'),
]