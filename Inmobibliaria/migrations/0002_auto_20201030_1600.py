# Generated by Django 2.2 on 2020-10-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inmobibliaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='mensaje',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='baños',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='dormitorios',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='habitaciones',
            field=models.IntegerField(),
        ),
    ]
