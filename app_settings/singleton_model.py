from django.db import models


class SingletonModel(models.Model):
    """
    Модель данных, которая всегда будет содержать только один объект, то есть только одну запись.
    Даёт возможность использовать информацию из этой модели прямо в шаблоне, без загрузки настроек сайта во view.
    Подробнее: https://evileg.com/ru/post/576/
    """
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Модель автоматически сохраняет все остальные при сохранении объекта,
        что позволяет всегда сохранять в базе только один экземпляр этой модели.
        """
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        """
        Берет из БД единственный объект настроек.
        Если объекта в БД нет, возвращает новый экземпляр этой модели, который нужно будет потом сохранить.
        """
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()
