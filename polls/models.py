from django.db import models


class TopFollowers(models.Model):
    top_1 = models.CharField(max_length=40, verbose_name='Первое место', )
    top_2 = models.CharField(max_length=40, verbose_name='Второе место', )
    top_3 = models.CharField(max_length=40, verbose_name='Третье место', )
    top_4 = models.CharField(max_length=40, verbose_name='Четвёртое место', )
    top_5 = models.CharField(max_length=40, verbose_name='Пятое место', )
    name = models.CharField(max_length=80, verbose_name='ФИО последоватлей')
    avatar = models.ImageField(upload_to='polls/images', verbose_name='Аватар создателя')
    bio = models.TextField(verbose_name='Краткая информация о последователях')

    def __str__(self):
        return f"Top of {self.name}"
