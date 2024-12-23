from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.teacher, name='teacher'),
    path('dashboard/', views.dashboard, name='dashboard')
]
