# Generated by Django 5.0.6 on 2024-06-03 23:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generator_message', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailschedule',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]