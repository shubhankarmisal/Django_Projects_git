from django.db import models

# Create your models here.
class librarybook(models.Model):
    l_name = models.CharField(max_length=50)
    l_author = models.CharField(max_length=50)
    l_img = models.ImageField()

def __str__(self):
    return f" {self.l_name} {self.l_author} {self.l_img}" 

class student(models.Model):
    s_name = models.CharField( max_length=50)    
    s_age = models.IntegerField()
    s_phone = models.IntegerField()

def __str__(self):
    return f" {self.s_name} {self.s_age} {self.s_phone}" 