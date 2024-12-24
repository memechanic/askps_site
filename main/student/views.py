from django.shortcuts import render, redirect
from .models import People, Attendance, Classes

def student(request):
    
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        class_id = request.POST.get('class_id')

        try:
            student = People.objects.get(login=login, isstudent=True)

            if student.password == password:
                request.session['student_id'] = student.id
                request.session['class_id'] = class_id
                return redirect('attendance')
            else:
                return render(request, 'student.html', {'error': 'Неверный пароль', 'class_id': class_id})

        except People.DoesNotExist:
            return render(request, 'student.html', {'error': 'Пользователь не найден', 'class_id': class_id})
    else:
        class_id = request.GET.get('class_id')
        return render(request, 'student.html', {'class_id': class_id})


def attendance(request):

    student_id = request.session.get('student_id')
    class_id = request.session.get('class_id')

    if not student_id:
        return redirect('student')

    student = People.objects.get(id=student_id)

    attendance_exist = Attendance.objects.filter(class_id=class_id, student_id=student_id)

    if not attendance_exist:

        attendance_record = Attendance.objects.create(
            class_id = class_id,
            student_id = student_id,
            qr_check = True,
            skud_check = True,
        )

        attendance_record.save()

    else:
        pass

    classes = []

    attendances = Attendance.objects.filter(student_id=student_id)

    for att in attendances:
        cls_id = att.class_id
        classes.append(
            Classes.objects.get(id=cls_id)
        )

    return render(request, 'attendance.html', {'student': student, 'classes': classes})