# Generated by Django 4.2.13 on 2024-06-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0036_problemmodel_location_of_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemmodel',
            name='backup',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
