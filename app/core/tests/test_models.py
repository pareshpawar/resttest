from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ Test creating new user with email"""
        email = 'test@pareshpawar.com'
        password = 'TestPass@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """ Test the email for normalizations """
        email = 'test@PARESHPAWAR.COM'
        user = get_user_model().objects.create_user(email, 'Pass@123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Pass@123')

    def test_create_new_superuser(self):
        """ Test Creating Superuser"""
        user = get_user_model().objects.create_superuser(
            'admin@pareshpawar.com',
            'Pass@123admin'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
