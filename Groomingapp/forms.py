from django import forms
from .models import Petdb, Detaildb 

class signupform(forms.ModelForm):
    class Meta:
        model=Petdb
        fields='__all__'

class detailform(forms.ModelForm):
    class Meta:
        model=Detaildb
        fields='__all__'
