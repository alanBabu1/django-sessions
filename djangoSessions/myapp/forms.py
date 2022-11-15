from django import forms
from django.core.validators import MinValueValidator

CHOICES = [('Male','Male'),('Female','Female'),('Others','Others')]
class Details(forms.Form):
    fullName = forms.CharField(
        max_length=100,
        required=True,
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
    )
    age = forms.IntegerField(
         validators=[MinValueValidator(18)]
    )
    gender=forms.CharField(
        label='Gender', 
        widget=forms.RadioSelect(choices=CHOICES))