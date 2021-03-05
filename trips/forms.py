from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Registration


class RegForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Введи свое имя"}),
                           label='Имя')
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': "Введи свою электронную почту", 'type': 'email'}),
        label='E-mail')

    phone = PhoneNumberField(label='Телефон', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "+7(999)999-99-99", 'type': 'tel',
               'pattern': "\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}"}))

    link = forms.URLField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Ссылка на твой профиль в соц. сети", 'type': 'url'}),
        label='E-mail')

    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone', 'link']


