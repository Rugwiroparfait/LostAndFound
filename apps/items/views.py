from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Item
from .serializers import ItemSerializer
from django.core.cache import cache

class ItemViewSet(viewsets.ModelViewSet):
    """
    ItemViewSet is a viewset for handling CRUD operations on Item objects.
    Attributes:
        serializer_class (ItemSerializer): The serializer class used for Item objects.
        permission_classes (list): List of permission classes that determine access control.
        filterset_fields (list): List of fields that can be used for filtering the queryset.
        search_fields (list): List of fields that can be used for searching the queryset.
        ordering_fields (list): List of fields that can be used for ordering the queryset.
    Methods:
        get_queryset(self):
            Returns the queryset of Item objects, prefetched with related images.
            Caches the queryset for 5 minutes to improve performance.
        perform_create(self, serializer):
            Saves the Item object with the user who created it.
    """
    serializer_class = ItemSerializer
    permission_classes=  [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['status', 'location']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'date_of_event']

    def get_queryset(self):
        """
        Retrieves the queryset of Item objects, prefetching related images.
        Caches the queryset to improve performance on subsequent requests.

        Returns:
            list: A list of Item objects, either from the cache or freshly queried.
        """
        queryset = Item.objects.all().prefetch_related('images')
        cache_key = f"items_list_{self.request .query_params}"
        cached_items = cache.get(cache_key)

        if cached_items is None:
            cached_items = list(queryset)
            cache.set(cache_key, cached_items, timeout=300)
        return cached_items
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
