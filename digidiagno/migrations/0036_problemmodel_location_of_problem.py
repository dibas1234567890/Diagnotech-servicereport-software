# Generated by Django 4.2.13 on 2024-06-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0035_problemmodel_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemmodel',
            name='location_of_problem',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]