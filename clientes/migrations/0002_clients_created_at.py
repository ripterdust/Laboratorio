# Generated by Django 4.1.7 on 2023-03-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
