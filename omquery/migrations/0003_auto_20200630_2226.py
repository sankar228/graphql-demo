# Generated by Django 3.0.7 on 2020-07-01 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omquery', '0002_auto_20200630_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cellom',
            old_name='enbom',
            new_name='enb',
        ),
    ]