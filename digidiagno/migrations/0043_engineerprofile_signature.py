# Generated by Django 4.2.13 on 2024-06-12 05:03

from django.db import migrations
import jsignature.fields


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0042_remove_engineerprofile_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineerprofile',
            name='signature',
            field=jsignature.fields.JSignatureField(null=True),
        ),
    ]
