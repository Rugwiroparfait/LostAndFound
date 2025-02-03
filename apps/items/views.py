from django.shortcuts import render
from rest_framework import generics, viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache
from rest_framework.exceptions import PermissionDenied

class ItemCreateView(generics.CreateAPIView):
    """
    Handles item creation.
    Only authenticated users can create items.
    """
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ItemUpdateView(generics.UpdateAPIView):
    """"
    Handles updating an existing item.
    Only the Item's owner can update it.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class ItemDeleteView(generics.DestroyAPIView):
    """
    Handles deleting an item.
    Only the Item's owner can delete it.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("You are not allowed to delete this item.")
        instance.delete()

class ItemListView(generics.ListAPIView):
    """
    Handles listing items with filtering, search, and caching
    Supports filtering by status and location.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'location']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'date_of_event']

class ItemDetailView(generics.RetrieveAPIView):
    """
    Handles retrieving a single item by its ID.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Item.objects.prefetch_related('user').all() or Item.objects.all().prefetch_related('images')