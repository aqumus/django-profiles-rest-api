from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """User Manager for Userprofile"""

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User should have email')
        
        # normalize second half of email id i.e in case of XXXX@YYY.com, normalize @YYY.com
        email = self.normalize_email(email)
        user = self.model(email=email, name= name)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """System User Database model"""
    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


class UserProfileStatusFeed(models.Model):
    """Feed model"""
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status_text = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.status_text} by {self.user_profile}'
