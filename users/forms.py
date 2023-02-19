from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
 
    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
 
 
class ProfileUpdateForm(forms.ModelForm):
    OPTIONS = (
        ("1", "Фотограф"),
        ("2", "Продюсер"),
        ("3", "Режиссер-постановщик"),
        ("4", "Оператор-постановщик"),
        ("5", "Художник-постановщик"),
        ("6", "Ассистенты"),
        ("7", "Монтажер"),
        ("8", "Vfx Специалист"),
        ("9", "Мобилограф"),
        ("10", "Другое")
    )
    category = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ),
        choices=OPTIONS,
        required=True,
        label="Выберите категорию"
    )

    class Meta:
        model = Profile
        fields = ['image', 'description', 'phone']