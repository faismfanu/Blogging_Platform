from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.register_url = reverse('register')
        self.register_url = reverse('login')

        self.user_data= {
            'username':"email@gmail.com",
            'first_name':"email@gmail.com",
            'last_name':"email@gmail.com",
            'email':"email@gmail.com",
            'password':"email@gmail.com"
        }
    
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()