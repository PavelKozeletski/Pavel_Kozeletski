# Generated by Django 4.1.2 on 2022-10-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0005_alter_model_submodels_avarege_maintenance_prise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_submodels',
            name='image',
            field=models.ImageField(upload_to='media/uploads'),
        ),
    ]
