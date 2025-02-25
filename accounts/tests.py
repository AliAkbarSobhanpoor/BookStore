from django.contrib.auth import get_user_model
from accounts.models import CustomUser
from django.test import TestCase

# Create your tests here.
User: CustomUser = get_user_model()

class CustomUserTests(TestCase):
    def test_create_user(self):

        user: CustomUser = User.objects.create_user(
            username="milad", email="email@email.com", password="password"
        )
        self.assertEqual(user.username, "milad")
        self.assertEqual(user.email, "email@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user: CustomUser = User.objects.create_superuser(
            username="admin", email="admin@admin.com", password="password"
        )
        self.assertEqual(admin_user.username, "admin")
        self.assertEqual(admin_user.email, "admin@admin.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
