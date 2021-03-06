# Generated by Django 3.0.7 on 2020-07-01 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnbOM',
            fields=[
                ('enb', models.IntegerField(max_length=500, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=500)),
                ('om10', models.DecimalField(blank=True, decimal_places=50, max_digits=1000)),
                ('om11', models.DecimalField(blank=True, decimal_places=50, max_digits=1000)),
                ('om12', models.DecimalField(blank=True, decimal_places=50, max_digits=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CellOM',
            fields=[
                ('cellid', models.IntegerField(max_length=500, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=500)),
                ('om1', models.DecimalField(blank=True, decimal_places=50, max_digits=1000)),
                ('om2', models.DecimalField(blank=True, decimal_places=50, max_digits=1000)),
                ('om3', models.DecimalField(blank=True, decimal_places=50, max_digits=1000)),
                ('om4', models.DecimalField(blank=True, decimal_places=50, max_digits=1000)),
                ('om5', models.DecimalField(blank=True, decimal_places=50, max_digits=1000)),
                ('enbom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='omquery.EnbOM')),
            ],
        ),
    ]
