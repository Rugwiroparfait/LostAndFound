from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.

    This model adds additional fields to the default User model provided by
    Django's authentication system. These fields include:
    - phone_number: A string field to store the user's phone number.
    - address: A text field to store the user's address.
    - created_at: A DateTime field to store when the user was created.
    - updated_at: A DateTime field to store when the user was last updated.

    Inherits from:
        AbstractUser: Provides default fields like username, email, first_name, last_name, etc.
    
    Meta options:
        ordering: Orders users by the most recent date_joined (descending)
    """
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_joined']
