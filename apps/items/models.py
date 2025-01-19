from django.db import models
from django.conf import settings

class Item(models.Model):
    """
    Model representing a lost/found item.

    This model is used to store information about items that users might 
    submit as lost or found. It includes fields for the title, description, 
    and timestamps for creation and updates.

    Fields:
        title: A CharField to store the title or name of the item.
        description: A TextField to store a detailed description of the item.
        created_at: A DateTimeField that automatically sets the timestamp when 
                    the item is created.
        updated_at: A DateTimeField that automatically updates the timestamp 
                    whenever the item is updated.

    Inherits from:
        models.Model: Django's base class for all models.
    """

    title =  models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass