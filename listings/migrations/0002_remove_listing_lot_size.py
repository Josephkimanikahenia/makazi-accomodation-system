# Generated by Django 2.2.13 on 2021-06-10 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='lot_size',
        ),
    ]
