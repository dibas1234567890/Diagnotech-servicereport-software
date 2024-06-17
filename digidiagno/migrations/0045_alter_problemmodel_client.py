# Generated by Django 4.2.13 on 2024-06-17 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0044_remove_clientmodel_signature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemmodel',
            name='client',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problem_client', to='digidiagno.clientmodel'),
        ),
    ]