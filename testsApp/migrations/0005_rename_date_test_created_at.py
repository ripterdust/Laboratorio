# Generated by Django 4.1.7 on 2023-03-11 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testsApp', '0004_alter_test_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='date',
            new_name='created_at',
        ),
    ]
