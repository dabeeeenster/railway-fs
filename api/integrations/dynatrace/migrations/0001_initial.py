# Generated by Django 3.2.12 on 2022-03-25 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environments', '0017_add_environment_api_key_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynatraceConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_url', models.URLField(null=True)),
                ('api_key', models.CharField(max_length=100)),
                ('entity_selector', models.CharField(max_length=1000)),
                ('environment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dynatrace_config', to='environments.environment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
