from django.db import models
from django.conf import settings

class Claim(models.Model):
    """
    Model representing a claim for a lost or found item.

    This model is used to store information about a claim made by a user 
    regarding a lost or found item. It includes fields for the timestamps 
    when the claim was created and last updated.

    Fields:
        id: An AutoField that automatically increments for each new claim.
        user_id: A ForeignKey to the user who made the claim.
        item_id: A ForeignKey to the item being claimed.
        status: A CharField to indicate the status of the claim.
        created_at: A DateTimeField that automatically sets the timestamp when 
                    the claim is created.
        updated_at: A DateTimeField that automatically updates the timestamp 
                    whenever the claim is modified.

    Inherits from:
        models.Model: Django's base class for all models.
    """
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_id = models.ForeignKey('items.Item', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)  # Increased max_length to 50
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)