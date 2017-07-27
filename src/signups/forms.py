from django import forms
from .models import SignUp
class SignUpForm(forms.ModelForm):
    class Meta:
        model=SignUp
        fields=['for_you','first_name','last_name','email']

#__all__
