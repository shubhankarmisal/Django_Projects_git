"""library_management URL Configuration

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
    path('addbook/', views.add_books, name='add-book'),
    path('updatebook/<int:id>', views.update_book, name='update-book'),
    path('deletebook/<int:id>', views.delete_book, name='delete-book'),
    path('addstudent/', views.student_table, name='student'),
    path('add_student/', views.add_student, name='add-student'),
    path('addstudent/updatestudent/<int:id>', views.update_student, name='update-student'),
    path('addstudent/deletetudent/<int:id>', views.delete_student, name='delete-student'),

]
