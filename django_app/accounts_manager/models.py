from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    user_id = models.AutoField(primary_key=True, unique=True)

    username = models.CharField(max_length=150, unique=True, blank=False, null=False,
                                help_text="Username in lowercase without spaces")

    email = models.EmailField(unique=True, blank=False, null=False, help_text="Email address")

    password = models.CharField(max_length=128, blank=False, null=False)

    def __str__(self):
        return self.username
