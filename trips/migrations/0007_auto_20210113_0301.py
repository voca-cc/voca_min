# Generated by Django 3.1.5 on 2021-01-13 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_trip_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roadmap',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Описание дня'),
        ),
    ]
