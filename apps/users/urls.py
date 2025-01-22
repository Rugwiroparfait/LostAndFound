from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import RegisterView, UserProfileView

urlpatterns = [
    path('register/' ,RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='Token_refresh'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]

