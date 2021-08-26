from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, models
from django.forms.widgets import PasswordInput, TextInput

User = get_user_model()
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= TextInput(
            attrs={
                "placeholder": "Username"
            }
        )
    )
    password = forms.CharField(
        widget=PasswordInput(
            attrs= {
                "class": "login-password",
                "id": "login-password",
                "placeholder": "Password"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact = username)
        if not qs.exists():
            raise forms.ValidationError("Invalid Username")
        return username


class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        widget=PasswordInput(
            attrs={
                "id": "register-password",
                "class": "register-password",
                "placeholder": "Password"
            }
        )
    )
    password2 = forms.CharField(
        widget=PasswordInput(
            attrs={
                "id": "register-password",
                "class": "register-password",
                "placeholder": "Confirm Your Password"
            }
        )
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username","email","password1","password2"]