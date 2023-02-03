from django.contrib import admin
from app1.models import Reservations
# Register your models here.

class MemberAdmin1(admin.ModelAdmin):
  list_display = ("s_name", "s_age", "s_phone","s_add")

admin.site.register(Reservations)
