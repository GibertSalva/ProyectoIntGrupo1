# Generated by Django 2.2 on 2020-11-13 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inmobibliaria', '0003_auto_20201112_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ubicacion',
            old_name='estado',
            new_name='provinia',
        ),
    ]
