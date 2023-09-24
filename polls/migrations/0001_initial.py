# Generated by Django 4.2.4 on 2023-09-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopFollowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_1', models.CharField(max_length=40, verbose_name='Первое место')),
                ('top_2', models.CharField(max_length=40, verbose_name='Второе место')),
                ('top_3', models.CharField(max_length=40, verbose_name='Третье место')),
                ('top_4', models.CharField(max_length=40, verbose_name='Четвёртое место')),
                ('top_5', models.CharField(max_length=40, verbose_name='Пятое место')),
                ('name', models.CharField(max_length=80, verbose_name='ФИО последоватлей')),
                ('avatar', models.ImageField(upload_to='polls/images', verbose_name='Аватар создателя')),
                ('bio', models.TextField(verbose_name='Краткая информация о последователях')),
            ],
        ),
    ]
