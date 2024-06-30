from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('ai-chatbot/', views.ai_chatbot, name='ai_chatbot'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('consultation/', views.consultation, name='consultation'),
    path('health-analytics/', views.health_analytics, name='health_analytics'),
]