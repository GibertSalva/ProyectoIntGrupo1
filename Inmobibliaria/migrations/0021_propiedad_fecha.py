# Generated by Django 2.2 on 2020-11-20 18:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Inmobibliaria', '0020_auto_20201120_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 11, 20, 18, 50, 56, 487753, tzinfo=utc)),
            preserve_default=False,
        ),
    ]