from __future__ import unicode_literals
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group
from django.core.mail import send_mail
from django.core.validators import RegexValidator, FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from .validators import avatar_size_validate


class User(AbstractBaseUser, PermissionsMixin):
    """
    Переопределенная модель пользователя.
    Обязательно в settings.py добавить AUTH_USER_MODEL = 'app_users.User'
    """
    email = models.EmailField(_('email'), unique=True)
    full_name = models.CharField(_('ФИО'), max_length=255, blank=True)
    date_joined = models.DateTimeField(_('дата регистрации'), auto_now_add=True)
    is_active = models.BooleanField(_('является активным'), default=True)
    is_staff = models.BooleanField(default=False, verbose_name=_('является сотрудником'))
    image_validator = FileExtensionValidator(
        allowed_extensions=['png', 'jpg', 'gif'],
        message=_('Ошибка загрузки: допускаются только файлы с расширением .jpg .gif .png')
    )
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True,
                               validators=[image_validator, avatar_size_validate])
    phone_regex = RegexValidator(regex=r'^\+\d{11,15}',
                                 message=_("Номер телефона должен быть в формате: '+79012345678'."))
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                    verbose_name=_('номер телефона'), unique=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('пользователи')

    def email_user(self, subject, message, from_email=None, **kwargs):
        """ Отправляет электронное письмо этому пользователю. """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class ProxyGroups(Group):
    """ Кастомная модель групп. """
    class Meta:
        proxy = True
        verbose_name = _('группа')
        verbose_name_plural = _('группы')
