from  django import forms
from .models import Cond
class CondForm(forms.ModelForm):
    class Meta:
        model = Cond
        fields = ('title','text','type','price')

