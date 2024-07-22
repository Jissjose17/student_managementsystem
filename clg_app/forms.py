from clg_app.models import studentform
from django import forms

class student(forms.ModelForm):
    class Meta:
        model=studentform
        fields='__all__'