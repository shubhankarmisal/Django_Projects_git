from app1.models import Reservations
from django import forms

class addReservations(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = '__all__'



