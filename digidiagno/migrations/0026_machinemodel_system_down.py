# Generated by Django 4.2.13 on 2024-05-31 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0025_rename_install_loc_machinemodel_install_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinemodel',
            name='system_down',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]