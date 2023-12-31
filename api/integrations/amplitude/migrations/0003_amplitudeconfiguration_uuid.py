# Generated by Django 3.2.13 on 2022-06-21 15:28

from django.db import migrations, models
import uuid

from core.migration_helpers import AddDefaultUUIDs


class Migration(migrations.Migration):

    dependencies = [
        ("amplitude", "0002_auto_20210325_1414"),
    ]

    operations = [
        migrations.AddField(
            model_name="amplitudeconfiguration",
            name="uuid",
            field=models.UUIDField(null=True, default=uuid.uuid4),
        ),
        migrations.RunPython(
            AddDefaultUUIDs("amplitude", "amplitudeconfiguration"),
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="amplitudeconfiguration",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
