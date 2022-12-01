# Generated by Django 4.0.4 on 2022-05-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bio_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport', models.FileField(upload_to='image')),
                ('national_identification_no', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('First_Name', models.CharField(max_length=50)),
                ('Other_Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=7)),
                ('Academic_level_Applying_for', models.IntegerField()),
                ('Date_Of_Birth', models.DateField(max_length=50)),
                ('State_Of_Origin', models.CharField(max_length=50)),
                ('LGA', models.CharField(max_length=50)),
                ('Permanent_Address', models.CharField(max_length=50)),
                ('Postal_Address', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Phone_Number', models.CharField(max_length=50)),
                ('Maritial_Status', models.CharField(choices=[('single', 'Single'), ('maried', 'Maried')], default='single', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='CURRENT_ACADEMIC_LEVEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_institution', models.CharField(max_length=50)),
                ('which_state_is_the_institution_located', models.CharField(max_length=50)),
                ('current_course', models.CharField(max_length=50)),
                ('year_of_admission', models.PositiveIntegerField(max_length=50)),
                ('category_of_study', models.CharField(choices=[('full-time', 'Full-Time'), ('part-time', 'Part-Time')], max_length=10)),
                ('current_level', models.CharField(choices=[('level-1', 'LEVEL-1'), ('level-2', 'LEVEL-2'), ('level-3', 'LEVEL-3'), ('level-4', 'LEVEL-4')], max_length=10)),
                ('current_CGPA', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NEXT_OF_KIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NEXT_OF_KIN_NAME', models.CharField(max_length=50)),
                ('NEXT_OF_KIN_OCCUPATION', models.CharField(max_length=50)),
                ('NEXT_OF_KIN_PHONE_NUMBER', models.CharField(max_length=50)),
                ('NEXT_OF_KIN_ADDRESS', models.CharField(max_length=50)),
                ('NEXT_OF_KIN_EMAIL', models.CharField(max_length=50)),
                ('NEXT_OF_KIN_RELATIONSHIP', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='upload_certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_identity_card', models.FileField(upload_to='image')),
                ('letter_of_admission_to_the_current_institution', models.FileField(upload_to='image')),
            ],
        ),
    ]