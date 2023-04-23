from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.utils import timezone 
from django.contrib.auth.models import User 
from django.template.defaultfilters import slugify


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(null=True, blank=True, max_length=200)
    business_id = models.CharField(null=True, blank=True, max_length=100)
    postal_code = models.CharField(null=True, blank=True, max_length=10)
    city = models.CharField(null=True, blank=True, max_length=100)
    phone = models.CharField(null=True, blank=True, max_length=100)
    email = models.EmailField(unique=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []