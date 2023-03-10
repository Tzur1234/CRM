from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username} | is_organisor: {self.is_organisor}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f' Organization follow: {self.user.username} '

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)    
    age = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    email = models.EmailField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=False)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    organization = models.ForeignKey('UserProfile', on_delete=models.CASCADE, null=True, blank=True)
    agent = models.ForeignKey("Agent",null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} | Agent: {self.agent}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey('UserProfile', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.username} | {self.organization}' 


class Category(models.Model):
    name = models.CharField(max_length=30)
    organization = models.ForeignKey("UserProfile", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} |{self.organization}'
    


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)
 


class MyModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)

class MyModel2(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)


    


