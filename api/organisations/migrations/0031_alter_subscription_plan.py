# Generated by Django 3.2.12 on 2022-05-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0030_alter_userorganisation_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='plan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
