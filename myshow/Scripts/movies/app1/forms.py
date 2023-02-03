from django import forms
from app1.models import movies, banner, theatre, addshow

class moviecreate(forms.ModelForm):
    class Meta:
        model = movies
        fields = '__all__'

class bannercreate(forms.ModelForm):
    class Meta:
        model = banner
        fields = '__all__' 

class theatrecreate(forms.ModelForm):
    class Meta:
        model = theatre
        fields = '__all__'   

class addshowcreate(forms.ModelForm):
    class Meta:
        model = addshow
        fields = '__all__'                    



