# Generated by Django 3.2.16 on 2022-12-12 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0035_add_organisation_subscription_information_cache'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.CharField(blank=True, default='free', max_length=100, null=True),
        ),
    ]
