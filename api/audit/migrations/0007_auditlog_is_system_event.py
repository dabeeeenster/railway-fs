# Generated by Django 3.2.16 on 2022-11-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0006_auditlog_master_api_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='is_system_event',
            field=models.BooleanField(default=False),
        ),
    ]
