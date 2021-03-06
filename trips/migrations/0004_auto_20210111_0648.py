# Generated by Django 3.1.5 on 2021-01-11 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_trip_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadmap',
            name='img_day',
            field=models.ImageField(null=True, upload_to='days', verbose_name='Изображение дня'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='price',
            field=models.PositiveIntegerField(null=True, verbose_name='Стоимость'),
        ),
    ]
