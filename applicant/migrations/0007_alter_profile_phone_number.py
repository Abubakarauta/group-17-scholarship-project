# Generated by Django 4.1.3 on 2022-11-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0006_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
