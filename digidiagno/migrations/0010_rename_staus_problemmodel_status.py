# Generated by Django 4.2.13 on 2024-05-21 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0009_problemmodel_staus_alter_problemmodel_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problemmodel',
            old_name='staus',
            new_name='status',
        ),
    ]
