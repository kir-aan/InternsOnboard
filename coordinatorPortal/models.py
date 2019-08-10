from django.db import models
from studentPortal.models import studentInternship
from django.contrib.auth.models import User

class finalApplicants(models.Model):
    company_Name = models.CharField(max_length=100,blank=False,null=True)
    student_Name = models.CharField(max_length=100,blank=False,null=True)
    accepted = models.BooleanField(default=False)
