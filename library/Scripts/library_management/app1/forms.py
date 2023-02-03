from app1.models import librarybook, student
from django import forms

class addlibrarybook(forms.ModelForm):
    class Meta:
        model = librarybook
        fields = '__all__'

class addstudent(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'

