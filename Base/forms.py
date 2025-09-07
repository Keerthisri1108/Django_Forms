from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class UnemploymentForm(forms.Form):
    name=forms.CharField(max_length=100)
    designation=forms.CharField(max_length=100)
    experience=forms.FloatField(validators=[validators.MinValueValidator(0)],min_value=0)
    current_ctc=forms.FloatField(min_value=0)
    email=forms.EmailField()
    phone=forms.CharField(validators=[validators.MinLengthValidator(10),validators.MaxLengthValidator(10)],max_length=10)
    address=forms.CharField(max_length=200)
    # manual validation
    def clean_experience(self):
        data=self.cleaned_data['experience']
        # check if the experience is valid,it should not 0 or negative number 
        if data>0:
            return data
        else:
            raise ValidationError("Invalid experience")
        
    def clean_name(self):
        data =self.cleaned_data['name']
        if data.isalpha():
            return data
        else:
            raise ValidationError("Name should only contain alphabets")




