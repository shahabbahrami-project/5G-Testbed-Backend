import uuid
import os
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
# class UserManager(BaseUserManager):
#
#     def create_user(self, email, password=None, **extra_fields):
#         """Creates and saves a new user"""
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     """Custom user model that supports email instead of username"""
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'


def user_image_file_path(instance, filename):
    """Generate file path for new user image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/user/', filename)


def site_image_file_path(instance, filename):
    """Generate file path for new site image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/site/', filename)


def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Creates and saves new superuser"""
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(null=True, upload_to=user_image_file_path)
    objects = UserManager()

    USERNAME_FIELD = 'email'


class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Recipe object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    ingredients = models.ManyToManyField('Ingredient')
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self):
        return self.title



class Urllc(models.Model):
    """Ingredient to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    TargetSNR = models.FloatField(default=0.0, null=False, blank=False)
    numberofUsers = models.IntegerField(default=1, null=False, blank=False)
    numerology = models.CharField(max_length=255, null=True, blank=True)
    sharedBandwidth = models.FloatField(default=0.0, null=False, blank=False)
    reservedBandwidth = models.FloatField(default=0.0, null=False, blank=False)
    channelGainShadowParam1 = models.FloatField(null=True, blank=True)
    channelGainFadeParam1 = models.FloatField(null=True, blank=True)
    channelGainFadeParam2 = models.FloatField(null=True, blank=True)
    power = models.FloatField(default=0.0, null=False, blank=False)
    trafficDist = models.CharField(max_length=150, null=True, blank=True)
    trafficParam1 = models.FloatField(null=True, blank=True)
    trafficParam2 = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
