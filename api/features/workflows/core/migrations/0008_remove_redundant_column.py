# Generated by Django 3.2.20 on 2023-07-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows_core', '0007_add_change_request_group_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changerequest',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalchangerequest',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
    ]
