# Generated by Django 4.1.7 on 2023-03-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_clients_nit'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
