# Generated by Django 2.2 on 2020-11-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inmobibliaria', '0005_auto_20201113_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='descripcion',
            field=models.TextField(max_length=200),
        ),
    ]