from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import User

class LoginForm(forms.Form):
    user_name = forms.CharField(required=True, label='Имя пользователя')
    password = forms.PasswordInput()
    
class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Ваш email')
    password_1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, help_text=password_validation.password_validators_help_text_html())
    password_2 = forms.CharField(label='Пароль (повторно)',widget=forms.PasswordInput, help_text='Введите ваш пароль повторно')
    
    def clean(self):
        super().clean()
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']
        if password_1 and password_2 and password_1 != password_2:
            errors = {'password_2': ValidationError ('Пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password_1'])
        user.is_active = True
        user.is_activated = True
        user.send_messages = False
        user.save()
        
        return user
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password_1', 'password_2')
        
        
class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'send_messages')