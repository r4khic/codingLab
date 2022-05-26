from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
    first_name = models.CharField(max_length=100, blank=True)
    second_name = models.CharField(max_length=100, blank=True)


class Profile(models.Model):
    profile_category = (
        ('Professor', 'Professor'),
        ('Student', 'Student'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_category = models.CharField(max_length=100, choices=profile_category, null=True, default='Student')
    nickname = models.CharField(max_length=100, blank=True)
    organization = models.CharField(max_length=100, blank=True)
    rating = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Organization(models.Model):
    organization_name = models.CharField(max_length=100, blank=True)
    about_organization = models.CharField(max_length=250, blank=True)
