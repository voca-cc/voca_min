# Generated by Django 3.1.5 on 2021-01-13 04:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0008_auto_20210113_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='included_coast',
            field=ckeditor.fields.RichTextField(verbose_name='В стоимость включено'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='not_included_coast',
            field=ckeditor.fields.RichTextField(verbose_name='В стоимость не включено'),
        ),
    ]