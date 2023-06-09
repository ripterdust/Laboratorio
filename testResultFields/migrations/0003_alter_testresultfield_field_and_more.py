# Generated by Django 4.1.7 on 2023-03-12 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsApp', '0007_test_comment'),
        ('fields', '0004_field_reference'),
        ('testResultFields', '0002_remove_testresultfield_measurment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresultfield',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fields.field'),
        ),
        migrations.AlterField(
            model_name='testresultfield',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsApp.test'),
        ),
    ]
