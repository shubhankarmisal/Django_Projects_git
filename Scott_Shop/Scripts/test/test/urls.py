"""test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('food/', views.index2, name='index2'),
    path('addfood/', views.add_food, name = 'add-food'),
    path('food/updatefood/<int:id>', views.update_food, name = 'update-food'),
    path('food/deletefood/<int:id>', views.delete_food, name = 'delete-food'),
    path('user/', views.index3, name='index3'),
    path('adduser/', views.add_user, name = 'add-user'),
    path('user/updateuser/<str:u_name>', views.update_user, name = 'update-user'),
    path('user/deleteuser/<str:u_name>', views.delete_user, name = 'delete-user'),
    path('addrev/', views.add_rev, name = 'add-rev'),
    path('updatereview/<int:u_name>', views.update_rev, name = 'update-review'),
    path('deletereview/<int:id>', views.delete_rev, name = 'delete-review'),
    path('register/', views.register_form, name = 'register'),
    path("login/", views.login_request, name="login"),
]
