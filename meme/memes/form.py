from django import forms
from .models import Meme

class memeform(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['title', 'image']