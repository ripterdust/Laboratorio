# Generated by Django 4.1.7 on 2023-03-11 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsApp', '0005_rename_date_test_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
