# Generated by Django 5.0.4 on 2024-05-07 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_address_constraint_address_unique_constraint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='deleted_at',
        ),
    ]