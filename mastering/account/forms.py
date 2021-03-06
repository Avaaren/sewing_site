from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords didn`t match!')
        else:
            return cd['password2']


