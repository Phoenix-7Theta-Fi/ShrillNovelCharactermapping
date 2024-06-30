from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('patient/', include('apps.patient_portal.urls')),
    path('doctor/', include('apps.doctor_portal.urls')),
    path('api/', include('apps.api.urls')),
]