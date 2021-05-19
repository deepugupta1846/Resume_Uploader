from django import forms
from .models import *

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female')
)
JOB_CITY_CHOICE = (
    ('Delhi', 'Delhi'),
    ('Pune', 'Pune'),
    ('Ranchi', 'Ranchi'),
    ('Mumbai', 'Mumbai'),
    ('Dhanbad', 'Dhanbad'),
    ('Banglore', 'Banglore'),
)


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Perferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }