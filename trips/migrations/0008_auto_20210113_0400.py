# Generated by Django 3.1.5 on 2021-01-13 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_auto_20210113_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='included_coast',
            field=models.TextField(verbose_name='В стоимость включено'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='not_included_coast',
            field=models.TextField(verbose_name='В стоимость не включено'),
        ),
    ]
