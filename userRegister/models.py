from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    usertype = models.CharField(max_length=2)
    # image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    def __str__(self):
        return self.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

