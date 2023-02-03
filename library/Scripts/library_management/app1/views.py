from django.shortcuts import render, redirect
from app1.models import librarybook, student
from app1.forms import addlibrarybook, addstudent
from django.http import HttpResponse
# Create your views here.

def index(request):
    l_data = librarybook.objects.all().values()
    lib = {
        'library': l_data
    }
    return render(request, 'index.html', lib)

def add_books(request):
    upload = addlibrarybook()
    if request.method == 'POST':
        upload = addlibrarybook(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'add_books.html', {'add_book':upload})     

def update_book(request, id):
    l_id = int(id)
    info = librarybook.objects.get(id = l_id) 
    details = addlibrarybook(request.POST or None , instance= info)
    if details.is_valid():
        details.save()
        return redirect('index') 
    return render(request, 'add_books.html', { 'add_book': details } )        

def delete_book(request, id):
    l_id = int(id)
    info = librarybook.objects.get(id = l_id)  
    info.delete()
    return redirect('index')  

def student_table(request):
    m_data = student.objects.all().values()
    th = {
        'student': m_data
    }
    return render(request, 'student.html', th)     

def add_student(request):
    upload = addstudent()
    if request.method == 'POST':
        upload = addstudent(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('student')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'add_student.html', {'add_student':upload})  


def update_student(request, id):
    l_id = int(id)
    info = student.objects.get(id = l_id) 
    details = addstudent(request.POST or None , instance= info)
    if details.is_valid():
        details.save()
        return redirect('student') 
    return render(request, 'add_student.html', { 'add_student': details } )  

def delete_student(request, id):
    s_id = int(id)
    info = student.objects.get(id = s_id)  
    info.delete()
    return redirect('student')      