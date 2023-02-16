# Generated by Django 4.1.7 on 2023-02-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='имя')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='email')),
                ('phone', models.CharField(max_length=10, verbose_name='телефон')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='сообщение')),
            ],
            options={
                'verbose_name': 'Форма обратной связи',
                'verbose_name_plural': 'Формы обратной связи',
            },
        ),
    ]
