from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate



class LoginForm(forms.Form):
    username = forms.CharField(max_length = 25);
    password = forms.CharField(widget = forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.authenticated_user = None;
        super(LoginForm, self).__init__(*args, **kwargs)
    
    def clean_username(self):
        data_username = self.cleaned_data['username']
        if User.objects.filter(username = data_username).count() != 1:
            raise forms.ValidationError('Invalid Username')
        return data_username

    def clean(self):
        data_username = self.cleaned_data.get('username', '')
        data_passwd = self.cleaned_data.get('password', '')
        user = authenticate(username=data_username, password = data_passwd)
        if data_username and data_passwd and not user:
            raise forms.ValidationError('Username/Password doesnot match')
        if user.is_active == False:
            raise form.ValidationError('Inactive User')
        self.authenticated_user = user
        return self.cleaned_data;