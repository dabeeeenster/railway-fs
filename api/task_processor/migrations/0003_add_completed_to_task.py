# Generated by Django 3.2.15 on 2022-08-24 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_processor', '0002_healthcheckmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterIndexTogether(
            name='task',
            index_together={('scheduled_for', 'num_failures', 'completed')},
        ),
    ]
