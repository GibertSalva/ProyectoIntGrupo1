# Generated by Django 2.2 on 2020-11-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inmobibliaria', '0019_auto_20201120_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='descripcion',
            field=models.TextField(max_length=2000),
        ),
    ]
