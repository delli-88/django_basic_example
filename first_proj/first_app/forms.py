from django import forms
from django.contrib.auth.models import User
from first_app.models import LocUser,AccessRecord,UserProfileInfo
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)

class NewUserForm(forms.ModelForm):
    passw = forms.CharField(widget = forms.PasswordInput)
    class Meta():
        model = LocUser
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username","email","password")

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ("portfolio_site",)
