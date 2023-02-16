from django.db import models


class FeedBack(models.Model):
    name = models.CharField('имя', max_length=200)
    email = models.EmailField('email', max_length=200, blank=True, null=True)
    phone = models.CharField('телефон', max_length=10)
    description = models.CharField('сообщение', max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"
