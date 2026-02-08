from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="البريد الإلكتروني"
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("هذا البريد الإلكتروني مستخدم بالفعل")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(
        label="اسم المستخدم",
        max_length=150
    )
    password = forms.CharField(
        label="كلمة المرور",
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("بيانات الدخول غير صحيحة")

        cleaned_data["user"] = user
        return cleaned_data
