# Generated by Django 4.1.7 on 2023-03-12 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_clients_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='nit',
            field=models.CharField(default='N/A', max_length=20),
        ),
    ]
