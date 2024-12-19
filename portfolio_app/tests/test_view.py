from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from portfolio_app.views import ContactView  # Ensure this import is correct

class ContactViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            password='password123',
            linkedin_url='https://www.linkedin.com/in/testuser',
            github_url='https://github.com/testuser'
        )

    def test_contact_view(self):
        response = self.client.get(reverse('contact', kwargs={'username': self.user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact Test User')
        self.assertContains(response, 'testuser@example.com')
        self.assertContains(response, 'https://www.linkedin.com/in/testuser')
        self.assertContains(response, 'https://github.com/testuser')
