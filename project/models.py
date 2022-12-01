from django.db import models

# Create your models here.
class scholarships(models.Model):
    Project_Name = models.CharField(max_length=50)
    status_choice = (
        ('active','ACTIVE'),
        ('unactive','UNACTIVE')
    )
    status = models.CharField(max_length=10, choices=status_choice, default='active')
    startin_date = models.DateTimeField()
    ending_date = models.DateTimeField()
    Picture = models.FileField(upload_to = 'image')
    content = models.TextField(max_length=150)

    def __str__(self):
        return self.Project_Name
