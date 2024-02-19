from django import forms
from .models import TestModel

class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ['title', 'description', 'image']
