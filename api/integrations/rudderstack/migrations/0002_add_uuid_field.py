# Generated by Django 3.2.13 on 2022-06-22 15:10

from django.db import migrations, models
import uuid

from core.migration_helpers import AddDefaultUUIDs


class Migration(migrations.Migration):

    dependencies = [
        ("rudderstack", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rudderstackconfiguration",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.RunPython(
            AddDefaultUUIDs("rudderstack", "rudderstackconfiguration"),
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="rudderstackconfiguration",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
