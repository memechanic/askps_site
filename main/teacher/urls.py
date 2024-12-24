from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.teacher, name='teacher'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/students', views.get_students, name='get_students'),
    path('api/students/add', views.add_student, name='add_student'),
    path('api/students/delete/<int:attendance_id>/', views.delete_student, name='delete_attendance'),
]
