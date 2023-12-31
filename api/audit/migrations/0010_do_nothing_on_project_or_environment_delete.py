# Generated by Django 3.2.16 on 2022-11-25 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0025_soft_delete_environments'),
        ('projects', '0016_soft_delete_projects'),
        ('audit', '0008_attach_historical_record_to_audit_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='environment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='audit_logs', to='environments.environment'),
        ),
        migrations.AlterField(
            model_name='auditlog',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='audit_logs', to='projects.project'),
        ),
    ]
