# Generated by Django 2.2 on 2022-03-06 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0006_auto_20220306_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regions', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=1500)),
            ],
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisement',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='region',
            field=models.ManyToManyField(related_name='advregion', to='advertisements.AdvertisementRegion'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='type',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advtype', to='advertisements.AdvertisementType'),
        ),
    ]
