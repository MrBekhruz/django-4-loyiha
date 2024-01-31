from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type':'datetime-local'})
       }