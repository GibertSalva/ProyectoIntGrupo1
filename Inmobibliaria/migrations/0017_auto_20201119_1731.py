# Generated by Django 2.2 on 2020-11-19 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inmobibliaria', '0016_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inmobibliaria.Propiedad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Consulta',
        ),
    ]