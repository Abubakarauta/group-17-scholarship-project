from PIL import Image as Im
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_team = models.BooleanField(default=False)
    role = models.CharField(max_length=20, default= '', blank=  True)
    reg_num = models.CharField(max_length=50, default= '', blank=  True)
    image = models.ImageField(upload_to='profile', default="", null=True, blank=True)
    phone_number= models.CharField(max_length= 11, default= '', blank=  True)

    def save(self): # new
        super().save()
        if self.image:
            img = Im.open(self.image.path)
            # resize it
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}' 

class Bio_data(models.Model):
    passport = models.FileField(upload_to='image')
    national_identification_no = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Other_Name = models.CharField(max_length=50)
    gender_choice = (
        ('male','Male'),
        ('female','Female')
    )
    Gender = models.CharField(max_length=7, choices=gender_choice, default='male')
    Academic_level_Applying_for = models.IntegerField()
    Date_Of_Birth = models.DateField(max_length=50)
    State_Of_Origin = models.CharField(max_length=50)
    LGA = models.CharField(max_length=50)
    Permanent_Address = models.CharField(max_length=50)
    Postal_Address = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50, )
    Phone_Number = models.CharField(max_length=50)
    maritial_choice = (
        ('single','Single'),
        ('maried','Maried')
    )
    Maritial_Status =  models.CharField(max_length=7, choices=maritial_choice, default='single')
    

    def __str__(self):
        return  self.surname + self.First_Name 

class NEXT_OF_KIN(models.Model):
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    relationship = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CURRENT_ACADEMIC_LEVEL(models.Model):
    current_institution = models.CharField(max_length=50)
    which_state_is_the_institution_located = models.CharField(max_length=50)
    current_course = models.CharField(max_length=50)
    year_of_admission = models.PositiveIntegerField()
    category_of_study_choice = (
        ('full-time','Full-Time'),
        ('part-time','Part-Time')
    )
    category_of_study = models.CharField(max_length=10, choices=category_of_study_choice)
    level_choice = (
        ('level-1','LEVEL-1'),
        ('level-2','LEVEL-2'),
        ('level-3','LEVEL-3'),
        ('level-4','LEVEL-4')
    )
    current_level = models.CharField(max_length=10, choices=level_choice)
    current_CGPA = models.PositiveIntegerField()

    def __str__(self):
        return self.current_institution

class upload_certificates(models.Model):
    school_identity_card = models.FileField(upload_to = 'image')
    letter_of_admission_to_the_current_institution = models.FileField(upload_to = 'image')

    def __str__(self):
        return self.school_identity_card