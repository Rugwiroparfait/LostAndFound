from django.db import models
from django.conf import settings

class Claim(models.Model):
    """
    Model representing a claim for a lost or found item.

    This model is used to store information about a claim made by a user 
    regarding a lost or found item. It includes fields for the timestamps 
    when the claim was created and last updated.

    Fields:
        created_at: A DateTimeField that automatically sets the timestamp when 
                    the claim is created.
        updated_at: A DateTimeField that automatically updates the timestamp 
                    whenever the claim is modified.

    Inherits from:
        models.Model: Django's base class for all models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)