# Generated by Django 5.2.1 on 2025-05-26 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='email',
        ),
    ]
