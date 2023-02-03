from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField( max_length=50, primary_key=True)
    useraddress = models.TextField()

def __str__(self):
    return f" {self.username} {self.useraddress}"


class fooditems(models.Model):
    foodname = models.CharField(max_length=50) 
    foodprice = models.IntegerField()

def __str__(self):
    return f" {self.foodname} {self.foodprice}"    

class reviews(models.Model):
    foodid = models.ForeignKey(user, on_delete=models.CASCADE)  
    reviewsname = models.CharField( max_length=50)   
    ratings = models.IntegerField()

def __str__(self):
    return f" {self.foodid} {self.reviewsname} {self.ratings}"     