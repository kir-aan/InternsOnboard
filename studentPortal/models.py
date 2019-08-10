from django.db import models
from InternsOnboardMain.models import internshipPost
from django.contrib.auth.models import User

class studentInternship(models.Model):
    companyName = models.ForeignKey(internshipPost,on_delete=models.CASCADE,null=True,db_column='companyName')
    studentName = models.ForeignKey(User,on_delete=models.CASCADE,null=True,db_column='studentName')
    applied = models.BooleanField(default=False)

    class Meta:
        db_table = 'studentInternship'
