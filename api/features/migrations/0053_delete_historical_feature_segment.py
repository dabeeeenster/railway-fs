# Generated by Django 3.2.17 on 2023-02-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0052_add_feature_state_value_audit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalFeatureSegment',
        ),
    ]
