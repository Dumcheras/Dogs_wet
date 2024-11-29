from django import forms
from users.models import User
from users.validators import validate_password
from django.contrib.auth.forms import PasswordChangeForm


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(StyleFormMixin, forms.ModelForm):
    model = User
    fields = ('email', 'first_name', 'last_name', 'phone',)


class UserRegisterForm(StyleFormMixin, forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите Пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        temp_data = self.cleaned_data
        validate_password(temp_data['password'])
        if temp_data['password'] != temp_data['password2']:
            print('Пароли не совпадают')
            raise forms.ValidationError('Пароли не совпадают')
        return temp_data['password2']


class UserLoginForm(StyleFormMixin, forms.Form):
    email = forms.EmailField(label='Введите адрес электронной почты')
    password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль')


class UserUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        exclude = ('is_active',)


class UserPasswordChangeForm(StyleFormMixin, PasswordChangeForm):
    pass
