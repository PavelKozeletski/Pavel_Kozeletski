# Generated by Django 4.1.2 on 2022-10-27 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0002_model_submodels_engine_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_submodels',
            name='model_submodel',
        ),
    ]
