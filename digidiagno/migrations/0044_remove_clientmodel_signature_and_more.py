# Generated by Django 4.2.13 on 2024-06-12 07:14

from django.db import migrations
import jsignature.fields


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0043_engineerprofile_signature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientmodel',
            name='signature',
        ),
        migrations.AddField(
            model_name='problemmodel',
            name='client_signature',
            field=jsignature.fields.JSignatureField(null=True),
        ),
    ]
