from django.urls import path
from . import views

urlpatterns = [
    path('ai-diagnosis/', views.ai_diagnosis, name='ai_diagnosis'),
    path('create-video-session/', views.create_video_session, name='create_video_session'),
]