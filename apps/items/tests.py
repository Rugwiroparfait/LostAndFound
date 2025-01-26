from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Item
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class ItemModelTestCase(TestCase):
    """Tests for the Item model."""

    def setUp(self):
        self.item = Item.objects.create(
            title="Lost Wallet",
            description="Black leather wallet lost at the park.",
            location="Central Park",
            status=Item.LOST,
            claim_status="unclaimed",
        )

    def test_item_creation(self):
        """Test that an Item instance is created correctly."""
        self.assertEqual(str(self.item), "Lost Wallet (LOST - unclaimed)")

    def test_item_default_values(self):
        """Test that default values are set correctly."""
        item = Item.objects.create(title="Lost Phone", description="A lost smartphone.")
        self.assertEqual(item.status, Item.LOST)
        self.assertEqual(item.claim_status, "unclaimed")
        self.assertEqual(item.location, "No Location")


class ItemViewSetTestCase(APITestCase):
    """Tests for the ItemViewSet."""

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)
        self.item = Item.objects.create(
            title="Lost Keys",
            description="A bunch of keys lost near the park.",
            location="Central Park",
            status=Item.LOST,
            claim_status="unclaimed"
        )

    def test_list_items(self):
        """Test retrieving a list of items."""
        response = self.client.get(reverse("item-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_item(self):
        """Test creating a new item."""
        item_data = {
            "title": "Lost Watch",
            "description": "Silver wristwatch lost at the gym.",
            "location": "Fitness Center",
            "status": Item.LOST,
            "claim_status": "unclaimed",
        }
        response = self.client.post(reverse("item-list"), item_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)

    def test_update_item(self):
        """Test updating an existing item."""
        updated_data = {"title": "Updated Keys"}
        response = self.client.patch(reverse("item-detail", kwargs={"pk": self.item.id}), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.title, "Updated Keys")

    def test_delete_item(self):
        """Test deleting an item."""
        response = self.client.delete(reverse("item-detail", kwargs={"pk": self.item.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)
