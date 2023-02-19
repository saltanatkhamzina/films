from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Введите заголовок объявления",
                "class": "form-control",
            }
        ),
        label="",
    )
    description = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Введите текст вашего объявления",
                "class": "form-control",
            }
        ),
        label="",
    )
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
    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form-control"
            }
        ),
        choices=OPTIONS,
        required=True,
        label="Выберите категории"
    )
    cost = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Введите предпологаемую цену"
            }
        ),
        label=""
    )

    class Meta:
        model = Ad
        exclude = ('approved', 'created', 'user', 'categories')

