# Generated by Django 5.1.2 on 2024-11-01 15:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
