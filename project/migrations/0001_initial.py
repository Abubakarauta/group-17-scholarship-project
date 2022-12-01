# Generated by Django 4.0.4 on 2022-05-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('active', 'ACTIVE'), ('unactive', 'UNACTIVE')], default='active', max_length=10)),
                ('startin_date', models.DateTimeField()),
                ('ending_date', models.DateTimeField()),
                ('Picture', models.FileField(upload_to='image')),
            ],
        ),
    ]
