# Generated by Django 3.2.9 on 2021-12-03 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timers', to='homework_api.assignment'),
        ),
    ]
