# Generated by Django 4.2.13 on 2024-05-23 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0011_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/img/report_uploads'),
        ),
    ]