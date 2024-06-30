from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def patient_dashboard(request):
    return render(request, 'patient_portal/dashboard.html')

@login_required
def ai_chatbot(request):
    # Placeholder for AI chatbot logic
    return render(request, 'patient_portal/ai_chatbot.html')

@login_required
def marketplace(request):
    # Placeholder for marketplace logic
    return render(request, 'patient_portal/marketplace.html')

@login_required
def consultation(request):
    # Placeholder for consultation logic
    return render(request, 'patient_portal/consultation.html')

@login_required
def health_analytics(request):
    # Placeholder for health analytics logic
    return render(request, 'patient_portal/health_analytics.html')