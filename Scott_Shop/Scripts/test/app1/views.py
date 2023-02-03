from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import user, fooditems, reviews
from app1.forms import usercreate, fooditemscreate, reviewscreate, Newuserform
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.

def index(request):
    r_data = reviews.objects.all().values()
    review = {
        'data': r_data
    }
    return render(request, 'index.html', review)

def index2(request):
    r_data = fooditems.objects.all().values()
    food_r = {
        'data2': r_data
    }
    return render(request, 'food.html', food_r)    

def add_food(request):
    upload = fooditemscreate()
    if request.method == 'POST':
        upload = fooditemscreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index2')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'add_food.html', {'add_food':upload}) 

def update_food(request, id):
    m_id = int(id)
    info = fooditems.objects.get(id = m_id) 
    details = fooditemscreate(request.POST or None , instance= info)
    if details.is_valid():
        details.save()
        return redirect('index2') 
    return render(request, 'add_food.html', { 'add_food': details } )   

def delete_food(request, id):
    m_id = int(id)
    info = fooditems.objects.get(id = m_id)  
    info.delete()
    return redirect('index2')     


def index3(request):
    r_data = user.objects.all().values()
    user_r = {
        'data3': r_data
    }
    return render(request, 'user.html', user_r)         

def add_user(request):
    upload = usercreate()
    if request.method == 'POST':
        upload = usercreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index3')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'add_user.html', {'add_user':upload})    


def update_user(request, u_name):
    m_id = str(u_name)
    info = user.objects.get(username = m_id) 
    details = usercreate(request.POST or None , instance= info)
    if details.is_valid():
        details.save()
        return redirect('index3') 
    return render(request, 'add_user.html', { 'add_user': details } )   

def delete_user(request, u_name):
    m_id = str(u_name)
    info = user.objects.get(username = m_id)  
    info.delete()
    return redirect('index3')       


def add_rev(request):
    upload = reviewscreate()
    if request.method == 'POST':
        upload = reviewscreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'update_review.html', {'add_review':upload})  


def update_rev(request, u_name):
    m_id = int(u_name)
    info = reviews.objects.get(id = m_id) 
    details = reviewscreate(request.POST or None , instance= info)
    if details.is_valid():
        details.save()
        return redirect('index') 
    return render(request, 'update_review.html', { 'add_review': details } )   

def delete_rev(request, id):
    m_id = int(id)
    info = reviews.objects.get(id = m_id)  
    info.delete()
    return redirect('index')                


def register_form(request):
    if request.method == 'POST':
        form = Newuserform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    form = Newuserform()
    return render(request, 'register.html', { 'register_form': form})                   


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password') 
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': form})  