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
        location: The manually provided location of the Item(where it actually found) DEFAULT('No Location').
        status: The state pof the item, Either 'Lost' or 'FOUND'.
        claim_status: the Claim state of the Item, such as 'CLAIMED', 'UNCLAIMED', or 'IN_PROCESS'.


    Inherits from:
        models.Model: Django's base class for all models.
    """
    LOST = 'LOST'
    FOUND = 'FOUND'
    STATUS_CHOICES = [
        (LOST, 'Lost'),
        (FOUND, 'Found'),
    ]

    CLAIM_STATUS_CHOICES = [
        ('unclaimed', 'Unclaimed'),
        ('claimed', 'Claimed'),
    ]

    title =  models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255, help_text="Enter the Item's location manually", default="No Location")
    #latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True ,help_text="Latitude (optional)")
    #longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, help_text="Longitude (optional)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='items')
    status = models.CharField(
        max_length=5,
        choices=STATUS_CHOICES,
        default=LOST # Default is 'lost'
    )

    claim_status = models.CharField(
        max_length=10,
        choices=CLAIM_STATUS_CHOICES,
        default='unclaimed'
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} ({self.status} - {self.claim_status})"