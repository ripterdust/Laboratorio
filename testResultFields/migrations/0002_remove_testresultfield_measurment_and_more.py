# Generated by Django 4.1.7 on 2023-03-11 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0003_alter_field_laboratory'),
        ('testResultFields', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresultfield',
            name='measurment',
        ),
        migrations.RemoveField(
            model_name='testresultfield',
            name='name',
        ),
        migrations.AddField(
            model_name='testresultfield',
            name='field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='fields.field'),
            preserve_default=False,
        ),
    ]