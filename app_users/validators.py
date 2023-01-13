from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def avatar_size_validate(value):
    """ Валидатор. Проверяет размер загружаемого изображения """
    image_size = value.size
    max_megabytes = 2.0
    if image_size > max_megabytes * 1024 * 1024:
        raise ValidationError(_(f"Ошибка загрузки: допускается размер файла не более {max_megabytes} MB"))


# class MyPasswordValidator:
#     """ Кастомный валидатор паролей """
#
#     def __init__(self):
#         self.template = r'(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{8,}'
#
#     def validate(self, password, user=None):
#         if not re.findall(self.template, password):
#             raise ValidationError(
#                 _("Пароль должен состоять минимум из 8 символов и содержать 1 цифру, "
#                   "одну букву в нижнем регистре и одну букву в верхнем регистре"),
#                 code='password_invalid'
#             )
#
#     def get_help_text(self):
#         return _("Пароль должен состоять минимум из 8 символов и содержать 1 цифру, "
#                  "одну букву в нижнем регистре и одну букву в верхнем регистре")
