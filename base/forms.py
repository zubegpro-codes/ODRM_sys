from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from base.models import Category, Location, Report, CustomUser, Comments

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser # Replace 'User' with the actual user model you are using
        fields = ['email', 'password1', 'password2', 'nin']



class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields= ['user','topic', 'title', 'Rimg', 'description', 'locate']

class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio','nin','avatar','phoneNo','address']


class Commentform(forms.Form):
    coment_body = forms.CharField(max_length=45,)

class Categoryform(ModelForm):
    class Meta:
        model= Category
        fields=['name']

