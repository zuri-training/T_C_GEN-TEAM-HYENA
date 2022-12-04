from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signinform(UserCreationForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    

    class meta:
        model = User
        fields = ('username', 'password')

        def save(self, comit=True):
            user = super(signinform, self).save(commit=False)
            user.username = self.cleaned_data['username']
            user.password = self.cleaned_data['password']

            if comit:
                User.save
            return User