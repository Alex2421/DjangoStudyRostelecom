# Generated by Django 4.2.8 on 2024-01-10 18:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_favorite_taste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='anouncement',
            field=models.TextField(default='', max_length=50, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Аннотация'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='', max_length=50, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=50, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Название'),
        ),
    ]