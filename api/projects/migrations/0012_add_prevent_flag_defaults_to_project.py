# Generated by Django 3.2.15 on 2022-09-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_add_uuid_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='prevent_flag_defaults',
            field=models.BooleanField(default=False, help_text='Prevent defaults from being set in all environments when creating a feature.'),
        ),
    ]
