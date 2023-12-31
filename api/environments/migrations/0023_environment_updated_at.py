# Generated by Django 3.2.16 on 2022-11-10 12:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0022_environment_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='environment',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Tracks changes to self and related entities, e.g. FeatureStates.'),
        ),
    ]
