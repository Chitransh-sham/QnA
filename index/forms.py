from django import forms
from .models import post

class post_form(forms.ModelForm):
    class Meta:
        model = post
        
       
        fields = ["question","post_image"]