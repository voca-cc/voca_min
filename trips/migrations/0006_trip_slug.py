# Generated by Django 3.1.5 on 2021-01-11 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20210111_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
