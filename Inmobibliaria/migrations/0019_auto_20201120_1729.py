# Generated by Django 2.2 on 2020-11-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inmobibliaria', '0018_auto_20201119_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='mensaje',
            field=models.TextField(max_length=2000),
        ),
    ]