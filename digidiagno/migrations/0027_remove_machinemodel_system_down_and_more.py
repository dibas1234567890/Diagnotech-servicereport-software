# Generated by Django 4.2.13 on 2024-05-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0026_machinemodel_system_down'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machinemodel',
            name='system_down',
        ),
        migrations.AddField(
            model_name='problemmodel',
            name='problem_area',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
        migrations.AddField(
            model_name='problemmodel',
            name='system_down',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
