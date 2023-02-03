from django.db import models

# Create your models here.

class Reservations(models.Model):
    s_name = models.CharField(max_length=50)
    s_age = models.IntegerField()
    s_phone = models.IntegerField()
    s_add = models.TextField()

def __str__(self):
    return f" {self.s_name} {self.s_age} {self.s_phone} {self.s_add}"     



