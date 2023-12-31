# Generated by Django 3.2.18 on 2023-06-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_merge_duplicate_permissions'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='userpermissiongroupprojectpermission',
            constraint=models.UniqueConstraint(fields=('group', 'project'), name='unique_group_project_permission'),
        ),
        migrations.AddConstraint(
            model_name='userprojectpermission',
            constraint=models.UniqueConstraint(fields=('user', 'project'), name='unique_user_project_permission'),
        ),
    ]
