from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


#Add serialization to this model

class internshipPost(models.Model):
    Uploader_info = models.CharField(max_length=100, editable=False, null = True)
    company_name = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=1000,blank=False)
    owner = models.ForeignKey(User, related_name="coordinatorName", on_delete=models.CASCADE, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.company_name
