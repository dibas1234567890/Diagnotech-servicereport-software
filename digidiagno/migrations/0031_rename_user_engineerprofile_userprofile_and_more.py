# Generated by Django 4.2.13 on 2024-06-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0030_engineerprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='engineerprofile',
            old_name='user',
            new_name='userprofile',
        ),
        migrations.AddField(
            model_name='engineerprofile',
            name='is_engineer',
            field=models.BooleanField(default=False),
        ),
    ]
