# Generated by Django 4.2.7 on 2023-11-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(max_length=221),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(max_length=221),
        ),
    ]
