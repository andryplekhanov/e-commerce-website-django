from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppReviewConfig(AppConfig):
    name = 'app_review'
    verbose_name = _('отзывы')
