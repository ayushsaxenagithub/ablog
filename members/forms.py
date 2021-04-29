from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            ]


class EditProfileForm (UserChangeForm):
    email = forms.EmailField (max_length=254, help_text='Enter a valid email address')
    first_name = forms.CharField (max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField (max_length=30, required=False, help_text='Optional')
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active=forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',

        ]

