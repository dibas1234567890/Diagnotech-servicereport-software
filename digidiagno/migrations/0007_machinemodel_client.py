# Generated by Django 5.0.4 on 2024-05-17 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0006_alter_machinemodel_machine_serial_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinemodel',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='machine', to='digidiagno.clientmodel'),
        ),
    ]
