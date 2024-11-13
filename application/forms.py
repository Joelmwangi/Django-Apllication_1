from django import forms
from application.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Age'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your gender'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Course'})

        }