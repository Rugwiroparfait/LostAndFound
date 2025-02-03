from django.urls import path
from .views import ItemCreateView, ItemUpdateView, ItemDeleteView, ItemListView, ItemDetailView

urlpatterns = [
    path('create/', ItemCreateView.as_view(), name='item-create'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='item-update'),
    path('delete/<int:pk>', ItemDeleteView.as_view(), name='item-delete'),  # No trailing slash
    path('list/', ItemListView.as_view(), name='item-list'),
]