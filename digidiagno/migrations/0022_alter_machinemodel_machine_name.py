# Generated by Django 4.2.13 on 2024-05-29 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0021_alter_problemmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinemodel',
            name='machine_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
