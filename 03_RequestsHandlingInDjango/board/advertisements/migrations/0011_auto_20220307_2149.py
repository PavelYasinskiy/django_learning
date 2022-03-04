# Generated by Django 2.2 on 2022-03-07 21:49

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0010_auto_20220307_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1500, verbose_name='Имя')),
                ('email', models.CharField(max_length=1500, verbose_name='Электронная почта')),
                ('phone', models.IntegerField(verbose_name='Телефон')),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='over_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 28, 21, 49, 18, 427196), verbose_name='Дата окончания публикации'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='public_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.AuthorContact', verbose_name='Автор'),
        ),
    ]
