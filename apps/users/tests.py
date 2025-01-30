from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User
from django.contrib.auth import get_user_model


User = get_user_model()

class UserTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')
        self.user = get_user_model().objects.create_user(
            username='existinguser',
            password='securepassword123',
            email='existinguser@example.com'
        )

    def test_register_user(self):
        response = self.client.post(self.register_url, {'username': 'testuser', 'password': 'securepassword123', 'email': 'testuser@example.com'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('username', response.data)
    #user registering done successfully
    
    def test_login_user(self):
        response = self.client.post(self.login_url, {'username': 'existinguser', 'password': 'securepassword123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    #login Tested successfully

    def test_profile_acess(self):
        self.client.login(username='existinguser', password='securepassword123')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('username', response.data)



