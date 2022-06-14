"""
Test for models
"""

from unittest import TestCase
from django.test import SimpleTestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        """Tests createing a user with email is successful"""
        email = "test@example.com"
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))