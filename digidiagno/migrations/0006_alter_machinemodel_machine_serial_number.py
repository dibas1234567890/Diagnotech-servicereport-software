# Generated by Django 5.0.4 on 2024-05-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0005_remove_machinemodel_machine_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinemodel',
            name='machine_serial_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
