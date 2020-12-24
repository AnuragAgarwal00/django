from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Addresses(models.Model):
    COUNTRY_CHOICES = (
        ('IND', 'India'),
        ('USA', 'America'),
        ('PAK', 'Pakistan'),
        ('SA', 'South_africa')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=250)
    pincode = models.CharField(max_length=50)
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES, default='IND')
    state = models.CharField(max_length=10, null=False)
    phone_no = models.CharField(max_length=15, null=False)


    def __str__(self):
        return f"{self.user.username} {self.street[0:4]}"