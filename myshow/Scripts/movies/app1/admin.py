from django.contrib import admin
from app1.models import movies, banner, theatre, addshow
# Register your models here.

class MemberAdmin1(admin.ModelAdmin):
  list_display = ("m_name", "m_picture", "m_Director", "m_discription",)

admin.site.register(movies,MemberAdmin1)

class MemberAdmin2(admin.ModelAdmin):
  list_display = ("b_name", "b_img", "b_info",)

admin.site.register(banner,MemberAdmin2)

class MemberAdmin3(admin.ModelAdmin):
  list_display = ("t_name", "t_location",)

admin.site.register(theatre,MemberAdmin3)

class MemberAdmin4(admin.ModelAdmin):
  list_display = ("t_name",)

admin.site.register(addshow,MemberAdmin4)