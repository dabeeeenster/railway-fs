# Generated by Django 3.2.16 on 2023-01-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIUsageBucket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_id', models.PositiveIntegerField()),
                ('resource', models.IntegerField(choices=[(1, 'Flags'), (2, 'Identities'), (3, 'Traits'), (4, 'Environment Document')])),
                ('total_count', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField()),
                ('bucket_size', models.PositiveIntegerField(help_text='Bucket size in minutes')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureEvaluationBucket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=2000)),
                ('environment_id', models.PositiveIntegerField()),
                ('total_count', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField()),
                ('bucket_size', models.PositiveIntegerField(help_text='Bucket size in minutes')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureEvaluationRaw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=2000)),
                ('environment_id', models.PositiveIntegerField()),
                ('evaluation_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='APIUsageRaw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.CharField(max_length=255)),
                ('resource', models.IntegerField(choices=[(1, 'Flags'), (2, 'Identities'), (3, 'Traits'), (4, 'Environment Document')])),
            ],
            options={
                'index_together': {('environment_id', 'created_at')},
            },
        ),
    ]
