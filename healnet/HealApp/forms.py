from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Blog

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'role', 'password1', 'password2']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter blog title"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 6, "placeholder": "Write your blog here..."}),
        }