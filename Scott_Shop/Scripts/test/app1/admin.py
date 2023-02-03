from django.contrib import admin
from app1.models import user, reviews, fooditems
# Register your models here.

class MemberAdmin1(admin.ModelAdmin):
  list_display = ("username", "useraddress",)

admin.site.register(user,MemberAdmin1)

class MemberAdmin2(admin.ModelAdmin):
  list_display = ("foodname", "foodprice",)

admin.site.register(fooditems,MemberAdmin2)

class MemberAdmin3(admin.ModelAdmin):
  list_display = ("foodid", "reviewsname","ratings",)

admin.site.register(reviews,MemberAdmin3)