from django import forms
from . models import Info
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Info
        fields= ('title','content')

class RegsiterNoteUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','password1','password2','email')