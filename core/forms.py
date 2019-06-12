from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from core.models import Contact, UploadScript


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=256, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(max_length=128, required=True)
    email = forms.CharField(max_length=256, required=True, widget=forms.EmailInput())
    # message = forms.TimeField(required=True)

    class Meta:
        model = Contact
        fields = '__all__'


class UploadScriptForm(forms.ModelForm):
    title = forms.CharField(max_length=128, required=True)

    class Meta:
        model = UploadScript
        fields = ['title', 'script_file']
