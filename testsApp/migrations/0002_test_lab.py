# Generated by Django 4.1.7 on 2023-03-11 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratories', '0002_laboratory_price'),
        ('testsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='lab',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='laboratories.laboratory'),
            preserve_default=False,
        ),
    ]