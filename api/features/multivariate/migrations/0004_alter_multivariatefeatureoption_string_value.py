# Generated by Django 3.2.12 on 2022-04-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multivariate', '0003_merge_20220131_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multivariatefeatureoption',
            name='string_value',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
    ]
