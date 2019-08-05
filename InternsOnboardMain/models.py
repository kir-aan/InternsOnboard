from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class internshipPost(models.Model):
    company_name = models.CharField(max_length=100)
    discription = models.CharField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company_name

