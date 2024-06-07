# Generated by Django 5.0.6 on 2024-06-01 20:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSchedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('department', models.CharField(choices=[('HR', 'Devisi HR'), ('RnD', 'Devisi RnD'), ('Media', 'Devisi Media Informasi'), ('Engineering', 'Devisi Engineering'), ('Customers', 'Customers')], max_length=50)),
                ('schedule_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
