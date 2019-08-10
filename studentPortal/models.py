from django.db import models
from InternsOnboardMain.models import internshipPost
from django.contrib.auth.models import User

class studentInternship(models.Model):
    companyName = models.ForeignKey(internshipPost,on_delete=models.CASCADE,null=True)
    studentName = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    applied = models.BooleanField(default=False)
