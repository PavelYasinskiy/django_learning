# Generated by Django 2.2 on 2022-03-04 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0003_auto_20220304_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='view_count',
            new_name='views_count',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]
