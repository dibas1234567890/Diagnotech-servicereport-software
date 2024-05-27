# Generated by Django 5.0.4 on 2024-05-19 09:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digidiagno', '0007_machinemodel_client'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('remarks', models.CharField(max_length=1024)),
                ('detailed_desc', models.CharField(max_length=2048)),
                ('name', models.CharField(max_length=50)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problem_client', to='digidiagno.clientmodel')),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('machine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problem_machine', to='digidiagno.machinemodel')),
            ],
        ),
    ]
