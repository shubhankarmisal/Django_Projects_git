from django.contrib import admin
from app1.models import librarybook, student
# Register your models here.

class MemberAdmin1(admin.ModelAdmin):
  list_display = ("l_name", "l_author", "l_img",)

admin.site.register(librarybook,MemberAdmin1)

class MemberAdmin2(admin.ModelAdmin):
  list_display = ("s_name", "s_age", "s_phone",)

admin.site.register(student,MemberAdmin2)
