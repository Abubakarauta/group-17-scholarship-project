# Generated by Django 4.1.3 on 2022-11-30 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0012_rename_user_profile_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='team',
            new_name='user',
        ),
    ]
