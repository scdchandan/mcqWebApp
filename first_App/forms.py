from django import forms
from django.contrib.auth.models import User
from first_App.models import UserProfileInfo

class UserForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Set a password'}), label='')
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder': 'Set a username'}), label='')
    first_name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder': 'Your First Name'}), label='')
    last_name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','placeholder': 'Your Last Name'}), label='')
    email = forms.CharField(widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Provide a valid EmailID'}), label='')

    class Meta():
            model = User
            fields = ('first_name','last_name','username', 'email', 'password')

    widgets = {
                'username': forms.TextInput(attrs={'class':'form-control'}),
                'email': forms.EmailInput(attrs={'class':'form-control'}),
            }

# class UserProfileInfoForm(forms.ModelForm):
#
#     class Meta():
#             model = UserProfileInfo
#             fields = ('profile_pic',)


# class NewUserForm(forms.ModelForm):
#     class Meta():
#         model = Users
#         fields = '__all__'
#
#         widgets = {
#             'name': forms.TextInput(attrs={'class':'form-control'}),
#             'email': forms.TextInput(attrs={'class':'form-control'}),
#             'password': forms.TextInput(attrs={'class':'form-control'})
#         }
