# Generated by Django 2.2.13 on 2021-06-10 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_remove_listing_lot_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='garage',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='sqft',
        ),
    ]
