from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f' Organization follow: {self.user.username}'

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)    
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=False)
    
    organization = models.ForeignKey('UserProfile', on_delete=models.CASCADE, null=True, blank=True)
    agent = models.ForeignKey("Agent",null=True, blank=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} | Agent: {self.agent}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey('UserProfile', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username} | {self.organization}' 


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)
 

def set_lead_organization(sender, instance, created, **kwargs):
    if created:
        instance.organization = UserProfile.objects.first()

post_save.connect(set_lead_organization, sender=Lead)
 




