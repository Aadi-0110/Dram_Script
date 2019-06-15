from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import modelformset_factory

from core.models import Contact, UploadScript, Character, TrainedModel, Script


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


class CharacterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('pkm')
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.fields['select_your_character'] = forms.ModelChoiceField(queryset=Character.objects.filter(script_id=pk), required=True)

    # select_your_character = forms.ModelChoiceField(queryset=Character.objects.filter(script_id=9), required=True)

    class Meta:
        fields = ['select_your_character']


class GenderForm(forms.ModelForm):
    character_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))

    class Meta:
        model = Character
        fields = ['character_name', 'character_gender']


GenderFormSet = modelformset_factory(Character, form=GenderForm)


class TrainedModelForm(forms.ModelForm):
    class Meta:
        model = TrainedModel
        fields = '__all__'


# class ScriptAudioForm(forms.ModelForm):
#     class Meta:
#         model = Script
#         fields = ['audio']
