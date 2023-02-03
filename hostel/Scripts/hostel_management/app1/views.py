from django.shortcuts import render, redirect
from app1.models import Reservations
from app1.forms import addReservations
from django.http import HttpResponse
# Create your views here.

def index(request):
    l_data = Reservations.objects.all().values()
    rev = {
        'data': l_data
    }
    return render(request, 'index.html', rev)

def add_student(request):
    upload = addReservations()
    if request.method == 'POST':
        upload = addReservations(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'add_student.html', {'add_student':upload})      

def update_student(request, id):
    l_id = int(id)
    info = Reservations.objects.get(id = l_id) 
    details = addReservations(request.POST or None , instance= info)
    if details.is_valid():
        details.save()
        return redirect('index') 
    return render(request, 'add_student.html', { 'add_student': details } )          


def delete_student(request, id):
    l_id = int(id)
    info = Reservations.objects.get(id = l_id)  
    info.delete()
    return redirect('index')  