# Generated by Django 4.2.13 on 2024-06-11 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('digidiagno', '0032_alter_engineerprofile_is_engineer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineerprofile',
            name='userprofile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
