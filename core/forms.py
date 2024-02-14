from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'category':forms.Select(attrs={'class':'form-control col-4'}),
            'name':forms.Select(attrs={'class':'form-control col-5'}),
            'image':forms.FileInput(attrs={'class':'form-control col-4'}),
            'content':forms.Textarea(attrs={'class':'form-control col-5 '})
       }