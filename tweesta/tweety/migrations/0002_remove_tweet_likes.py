# Generated by Django 5.1.4 on 2025-01-13 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweety', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='likes',
        ),
    ]
