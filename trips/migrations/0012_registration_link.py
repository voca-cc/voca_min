# Generated by Django 3.1.5 on 2021-02-08 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0011_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Соц.сети'),
        ),
    ]