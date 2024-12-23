from django.shortcuts import render, redirect
from .models import People

# Create your views here.
def teacher(request):
    
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('pass')

        try:
            teacher = People.objects.get(login=login, isteacher=True)
            
            if teacher.password == password:
                request.session['user_login'] = teacher.fio
                request.session['class_id'] = 1
                return redirect('dashboard')
            else:
                return render(request, 'teacher.html', {'error': 'Неверный пароль'})
            
        except People.DoesNotExist:
            return render(request, 'teacher.html', {'error': 'Пользователь не найден'})

    return render(request, 'teacher.html')

def dashboard(request):

    user_login = request.session.get('user_login', None)
    class_id = request.session.get('class_id')

    if user_login is None: return redirect('teacher')
    
    if 'logout' in request.POST:
        del request.session['user_login']
        return redirect('teacher')

    return render(request, 'dashboard.html', {'user_login': user_login, 'class_id': class_id})