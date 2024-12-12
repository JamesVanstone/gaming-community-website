from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.role_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clan = models.TextField(max_length=50, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    preferred_role = models.ForeignKey(
            Role,
            on_delete=models.SET_NULL,
            null=True,
            blank=True
        )
    
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
