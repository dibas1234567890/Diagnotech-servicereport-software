# Generated by Django 4.2.13 on 2024-05-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0016_profile_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinemodel',
            name='model',
            field=models.CharField(choices=[('E411', 'E411'), ('Ventana', 'Ventana'), ('C311', 'C311')], default='Processing', max_length=100),
        ),
    ]
