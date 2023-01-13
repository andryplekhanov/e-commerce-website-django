from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm, \
    AuthenticationForm
from django.utils.translation import gettext_lazy as _


class CreationUserForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=False, label=_('ФИО'),
                                widget=forms.TextInput(attrs={
                                    'class': 'form-input',
                                    'data-validate': 'require',
                                    'placeholder': _('Введите ФИО'),
                                    'maxlength': '255'
                                }))
    avatar = forms.ImageField(required=False, label=_('Аватар'),
                              widget=forms.ClearableFileInput(attrs={
                                  'class': 'Profile-file form-input',
                                  'type': 'file',
                                  'accept': '.jpg,.gif,.png',
                                  'data-validate': 'onlyImgAvatar'
                              }))
    email = forms.EmailField(max_length=250, label='email', required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-input',
                                 'data-validate': 'requireMail',
                                 'maxlength': '250'
                             }))
    password1 = forms.CharField(max_length=150, required=True, label=_('Пароль'),
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-input',
                                    'data-validate': 'requirePassword',
                                    'placeholder': _('Введите пароль'),
                                    'autocomplete': 'new-password',
                                    'maxlength': '150'
                                }))
    password2 = forms.CharField(max_length=150, required=True, label=_('Подтверждение пароля'),
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-input',
                                    'data-validate': 'requireRepeatPassword',
                                    'placeholder': _('Введите пароль еще раз'),
                                    'autocomplete': 'new-password',
                                    'maxlength': '150'
                                }))
    phone_number = forms.CharField(required=False, label=_('Номер телефона'),
                                   widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'full_name', 'phone_number', 'avatar')


class UserChangingForm(UserChangeForm):
    full_name = forms.CharField(max_length=255, required=False, label=_('ФИО'),
                                widget=forms.TextInput(attrs={
                                    'class': 'form-input',
                                    'data-validate': 'require',
                                    'placeholder': _('Введите ФИО'),
                                    'maxlength': '255'
                                }))
    avatar = forms.ImageField(required=False, label=_('Аватар'),
                              widget=forms.ClearableFileInput(attrs={
                                  'class': 'Profile-file form-input',
                                  'type': 'file',
                                  'accept': '.jpg,.gif,.png',
                                  'data-validate': 'onlyImgAvatar',
                              }))
    email = forms.EmailField(max_length=250, label='email', required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-input',
                                 'data-validate': 'require',
                                 'maxlength': '250'
                             }))
    password1 = forms.CharField(max_length=150, required=True, label=_('Пароль'),
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-input',
                                    'data-validate': 'requirePassword',
                                    'placeholder': _('Введите пароль'),
                                    'autocomplete': 'new-password',
                                    'maxlength': '150'
                                }))
    password2 = forms.CharField(max_length=150, required=True, label=_('Подтверждение пароля'),
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-input',
                                    'data-validate': 'requireRepeatPassword',
                                    'placeholder': _('Введите пароль еще раз'),
                                    'autocomplete': 'new-password',
                                    'maxlength': '150'
                                }))
    phone_number = forms.CharField(required=False, label=_('Номер телефона'),
                                   widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'full_name', 'phone_number', 'avatar')


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=250, required=True, label='email',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-input',
                                    'data-validate': 'require',
                                    'maxlength': '250',
                                    'placeholder': _('Введите e-mail'),
                                    'autocomplete': 'email'
                                }))
    password = forms.CharField(max_length=150, label=_('Пароль'), required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-input',
                                   'data-validate': 'require',
                                   'placeholder': _('Введите пароль'),
                                   'autocomplete': 'password',
                                   'maxlength': '150'}))


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(max_length=250, required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-input',
                                 'data-validate': 'require',
                                 'maxlength': '250',
                                 'autocomplete': 'email'
                             }))


class PasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=150, strip=False, required=True,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-input',
                                        'data-validate': 'requirePassword',
                                        'placeholder': _('Введите пароль'),
                                        'autocomplete': 'new-password',
                                        'maxlength': '150'
                                    }))
    new_password2 = forms.CharField(max_length=150, required=True, strip=False,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-input',
                                        'data-validate': 'requireRepeatPassword',
                                        'placeholder': _('Введите пароль еще раз'),
                                        'autocomplete': 'new-password',
                                        'maxlength': '150'
                                    }))
