from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class EnquiryData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()

    SKILLS_CHOICES=(('py','Python'),
                   ('dj','Django'),
                   ('fl','Flask'),
                   ('ri','RestApi'))
    skills=MultiSelectField(max_length=200,choices=SKILLS_CHOICES)

    LOCATIONS_CHOICES=(('hy','HYDERBAD'),
                       ('bg','BANGALORE'),
                       ('ch','CHENNI'),
                       ('mu','MUMBAI'))
    locations=MultiSelectField(max_length=200,choices=LOCATIONS_CHOICES)

    gender=models.CharField(max_length=100)
    date=models.DateField(max_length=100)
