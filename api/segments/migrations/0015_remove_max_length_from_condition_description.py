# Generated by Django 3.2.16 on 2022-12-19 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0014_add_description_to_segment_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
