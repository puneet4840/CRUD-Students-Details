from django.core import validators
from django import forms
from . models import Student

class Student_Form(forms.ModelForm):
    # name=forms.CharField(max_length=70)
    # email=forms.EmailField(max_length=70)
    # password=forms.CharField(max_length=70,widget=forms.PasswordInput)
    class Meta:
        model=Student
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }

