# Generated by Django 3.1.5 on 2021-01-26 02:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0009_auto_20210113_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourauthor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='tourauthor',
            name='facebook_link',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='tourauthor',
            name='instagram_link',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='tourauthor',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='tourauthor',
            name='telegram_link',
            field=models.URLField(blank=True, null=True, verbose_name='Telegram'),
        ),
        migrations.AddField(
            model_name='tourauthor',
            name='vk_link',
            field=models.URLField(blank=True, null=True, verbose_name='Vk'),
        ),
    ]
