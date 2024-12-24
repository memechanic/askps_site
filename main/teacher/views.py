from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import People, Classes, Attendance
import json

# Create your views here.
def teacher(request):
    
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('pass')

        try:
            teacher = People.objects.get(login=login, isteacher=True)
            
            if teacher.password == password:
                request.session['teacher_id'] = teacher.id
                request.session['teacher_fio'] = teacher.fio
                request.session['class_id'] = 1
                return redirect('dashboard')
            else:
                return render(request, 'teacher.html', {'error': 'Неверный пароль'})
            
        except People.DoesNotExist:
            return render(request, 'teacher.html', {'error': 'Пользователь не найден'})

    return render(request, 'teacher.html')

def dashboard(request):

    teacher_id = request.session.get('teacher_id', None)
    teacher_fio = request.session.get('teacher_fio', None)
    class_id = request.session.get('class_id')

    if teacher is None: return redirect('teacher')
    
    if 'logout' in request.POST:
        del request.session['teacher_id']
        del request.session['teacher_dio']
        return redirect('teacher')

    return render(request, 'dashboard.html', {'teacher_id': teacher_id, 'teacher_fio': teacher_fio, 'class_id': class_id})

def get_students(request):
    if request.method == 'GET':

        class_id = request.session.get('class_id')
        attendances = Attendance.objects.filter(class_id=class_id)

        students = []

        for att in attendances:
            stud_id = att.student_id
            stud = People.objects.get(id=stud_id, isstudent=True)
            students.append({
                'name': stud.fio, 
                'attendance_id': att.id,
            })

        return JsonResponse({'students': students}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def add_student(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        student_fio = data.get('name')
        class_id = request.session.get('class_id')

        if not class_id or not student_fio:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        student = People.objects.get(fio=student_fio, isstudent=True)

        Attendance.objects.create(
            class_id=class_id,
            student_id=student.id,
            qr_check=True,
            skud_check=True,
        )

        return JsonResponse({'success': True})
    
    else:
        return JsonResponse({'error': 'Not Allowed'}, status=405)

def delete_student(request, attendance_id):
    if request.method == 'DELETE':
        try:
            attendance = Attendance.objects.get(id=attendance_id)
            attendance.delete()
            return JsonResponse({'success': True}, status=200)
        except Attendance.DoesNotExist:
            return JsonResponse({'error': 'Attendance record not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)