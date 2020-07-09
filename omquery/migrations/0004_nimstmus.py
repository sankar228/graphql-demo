# Generated by Django 3.0.7 on 2020-07-06 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omquery', '0003_auto_20200630_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='NimsTmus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(blank=True, max_length=500, null=True)),
                ('oss_market', models.CharField(blank=True, max_length=500, null=True)),
                ('vendor', models.CharField(blank=True, max_length=50, null=True)),
                ('technology', models.CharField(blank=True, max_length=50, null=True)),
                ('site_name', models.CharField(blank=True, max_length=500, null=True)),
                ('gnodeb_id', models.CharField(blank=True, max_length=50, null=True)),
                ('cellname', models.CharField(blank=True, max_length=50, null=True)),
                ('gnodeb_name', models.CharField(blank=True, max_length=50, null=True)),
                ('cell_id', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zip', models.CharField(blank=True, max_length=50, null=True)),
                ('coveragetype', models.CharField(blank=True, max_length=100, null=True)),
                ('RF_Solution', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude_sector', models.IntegerField(blank=True, null=True)),
                ('longitude_sector', models.IntegerField(blank=True, null=True)),
                ('azimuth', models.CharField(blank=True, max_length=100, null=True)),
                ('horizontal_bw', models.CharField(blank=True, max_length=100, null=True)),
                ('vertical_bw', models.CharField(blank=True, max_length=100, null=True)),
                ('antenna_height_ft', models.IntegerField(blank=True, null=True)),
                ('antenna_gain', models.CharField(blank=True, max_length=100, null=True)),
                ('antenna_model', models.CharField(blank=True, max_length=100, null=True)),
                ('propagation_model', models.CharField(blank=True, max_length=100, null=True)),
                ('rs_power', models.CharField(blank=True, max_length=100, null=True)),
                ('pa_power', models.CharField(blank=True, max_length=100, null=True)),
                ('electrical_tilt', models.CharField(blank=True, max_length=100, null=True)),
                ('mcc', models.IntegerField(blank=True, null=True)),
                ('mnc', models.IntegerField(blank=True, null=True)),
                ('lac', models.CharField(blank=True, max_length=100, null=True)),
                ('sectorname', models.CharField(blank=True, max_length=100, null=True)),
                ('tac', models.CharField(blank=True, max_length=100, null=True)),
                ('pci', models.CharField(blank=True, max_length=100, null=True)),
                ('carrier_nm', models.CharField(blank=True, max_length=100, null=True)),
                ('oss', models.CharField(blank=True, max_length=100, null=True)),
                ('cell_status', models.CharField(blank=True, max_length=100, null=True)),
                ('on_airdate', models.CharField(blank=True, max_length=100, null=True)),
                ('ul_ch_bw', models.CharField(blank=True, max_length=100, null=True)),
                ('dl_ch_bw', models.CharField(blank=True, max_length=100, null=True)),
                ('earfcn_dl', models.CharField(blank=True, max_length=100, null=True)),
                ('earfcn_ul', models.CharField(blank=True, max_length=100, null=True)),
                ('NED_export_date', models.CharField(blank=True, max_length=100, null=True)),
                ('gnodeb_status', models.CharField(blank=True, max_length=100, null=True)),
                ('Site_Type', models.CharField(blank=True, max_length=100, null=True)),
                ('TimeZone', models.CharField(blank=True, max_length=100, null=True)),
                ('Cell_Type', models.CharField(blank=True, max_length=100, null=True)),
                ('sector_id', models.IntegerField(blank=True, null=True)),
                ('Carrier_id', models.IntegerField(blank=True, null=True)),
                ('cgi', models.CharField(blank=True, max_length=100, null=True)),
                ('Band', models.CharField(blank=True, max_length=100, null=True)),
                ('antenna_agl_ft', models.CharField(blank=True, max_length=100, null=True)),
                ('total_loss', models.CharField(blank=True, max_length=100, null=True)),
                ('mechanical_tilt', models.CharField(blank=True, max_length=100, null=True)),
                ('Cell_Radius', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]