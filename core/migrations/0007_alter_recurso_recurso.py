# Generated by Django 4.1.6 on 2023-08-15 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_recurso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='recurso',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
    ]
