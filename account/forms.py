__author__ = 'jeffrey'

from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    username = forms.RegexField(label=("Username"), max_length=30, regex=r'^[\w.@+-]+$', help_text = '', error_messages = {'invalid': ("This value may contain only letters, numbers and @/./+/-/_ characters.")})

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self,commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)
        #user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user