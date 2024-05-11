from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.conf import settings
import jwt
from accounts.views import RegisterView, LoginView

class RegisterViewTest(APITestCase):

    def test_register_user(self):
        url = reverse('register')

        user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
        }

        response = self.client.post(url, user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')

    def test_register_user_with_missing_data(self):
        url = reverse('register')

        incomplete_user_data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        response = self.client.post(url, incomplete_user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_with_existing_username(self):
        User.objects.create_user(username='testuser', password='password')

        url = reverse('register') 

        existing_username_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
        }

        response = self.client.post(url, existing_username_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_with_existing_email(self):
        User.objects.create_user(username='existinguser', email='test@example.com', password='password')

        url = reverse('register')

        existing_email_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
        }

        response = self.client.post(url, existing_email_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_with_weak_password(self):
        url = reverse('register')

        weak_password_data = {
            'username': 'testuser',
            'password': '123456',  
            'email': 'test@example.com',
        }

        response = self.client.post(url, weak_password_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class LoginViewTest(APITestCase):
    def test_login_user(self):
        # Create a user for testing login
        user = User.objects.create_user(username='testuser', password='testpassword')

        url = reverse('login')  # Generates the URL for the 'login' view

        # Define the login data
        login_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        response = self.client.post(url, login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

        # Verify the JWT token
        token = response.data['token']
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
        self.assertEqual(payload['username'], 'testuser')

    def test_login_with_invalid_credentials(self):
        url = reverse('login')  # Generates the URL for the 'login' view

        # Define invalid login data
        invalid_login_data = {
            'username': 'testuser',
            'password': 'invalidpassword',
        }

        response = self.client.post(url, invalid_login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_with_missing_data(self):
        url = reverse('login')

        incomplete_login_data = {
            'password': 'testpassword',
        }

        response = self.client.post(url, incomplete_login_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


        