# Generated by Django 2.0.1 on 2019-10-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_person_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
