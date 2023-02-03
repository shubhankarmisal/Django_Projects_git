from django.db import models

# Create your models here.
class movies(models.Model):
    m_name = models.CharField(max_length=50)
    m_picture = models.ImageField()
    m_Director = models.CharField(max_length=50)
    m_discription = models.TextField()

def __str__(self):
    return f" {self.m_name} {self.m_picture} {self.m_Director} {self.m_discription}"

class banner(models.Model):
    b_name = models.CharField(max_length=50)
    b_img = models.ImageField()
    b_info = models.TextField()

def __str__(self):
    return f" {self.b_name} {self.b_img} {self.b_info}"    

class theatre(models.Model):
    t_name = models.CharField(max_length=50, primary_key=True)
    t_location = models.CharField(max_length=50)

def __str__(self):
    return f" {self.t_name} {self.t_location}"    

class addshow(models.Model):
    t_name = models.ForeignKey(theatre, on_delete=models.CASCADE)

def __str__(self):
    return f" {self.t_name}"     


