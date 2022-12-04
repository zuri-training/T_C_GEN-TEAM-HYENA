from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signupform(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(label='E-mail')

    class meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name',)

        def save(self, comit=True):
            user = super(signupform, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']

            if comit:
                User.save
            return User