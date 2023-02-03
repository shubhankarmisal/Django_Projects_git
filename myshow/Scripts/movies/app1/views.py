from django.shortcuts import render, redirect
from app1.models import movies, banner, theatre, addshow
from django.http import HttpResponse
from app1.forms import moviecreate, bannercreate, theatrecreate, addshowcreate

# Create your views here.

def index(request):
    m_data = movies.objects.all().values()
    movie = {
        'movie': m_data
    }
    return render(request, 'index.html', movie)




def addmovie(request):
    upload = moviecreate()
    if request.method == 'POST':
        upload = moviecreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'add_movie.html', {'add_movie':upload})         


def update_movie(request, id):
    m_id = int(id)
    info = movies.objects.get(id = m_id) 
    details = moviecreate(request.POST or None , instance= info)
    if details.is_valid():
        details.save()
        return redirect('index') 
    return render(request, 'add_movie.html', { 'add_movie': details } )  


def delete_movie(request, id):
    m_id = int(id)
    info = movies.objects.get(id = m_id)  
    info.delete()
    return redirect('index')        


def addbanner(request):
    upload = bannercreate()
    if request.method == 'POST':
        upload = bannercreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'add_banner.html', {'add_banner':upload}) 


def theatre_table(request):
    m_data = theatre.objects.all().values()
    th = {
        'theatre': m_data
    }
    return render(request, 'theatre.html', th)


def add_theatre(request):
    upload = theatrecreate()
    if request.method == 'POST':
        upload = theatrecreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('theatre')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'add_theatre.html', {'add_theatre':upload})    


def show_table(request):
    m_data = addshow.objects.all().values()
    th = {
        'show': m_data
    }
    return render(request, 'updateshows.html', th)



def add_show(request):
    upload = addshowcreate()
    if request.method == 'POST':
        upload = addshowcreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'add_show.html', {'add_show':upload}) 