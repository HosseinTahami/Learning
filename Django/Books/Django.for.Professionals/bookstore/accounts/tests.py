from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from . import views


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="test-user", email="test@email.com", password="secret"
        )
        self.assertEqual(user.username, "test-user")
        self.assertEqual(user.email, "test@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="admin-test-user", email="test@email.com", password="secret"
        )
        self.assertEqual(admin_user.username, "admin-test-user")
        self.assertEqual(admin_user.email, "test@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


# class SignUpTests(TestCase):

#     def setUp(self):
#         self.url = reverse("signup")
#         self.response = self.client.get(self.url)

#     def test_signup_template(self):
#         self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(self.response, "registration/signup.html")
#         self.assertContains(self.response, "Sign Up")
#         self.assertNotContains(self.response, "Hi I am not here.")

#     def test_signup_form(self):
#         form = self.response.context.get("form")
#         self.assertIsInstance(form , CustomUserCreationForm)
#         self.assertContains(self.response, "csrfmiddlewaretoken")

#     def test_signup_view(self):
#         view = resolve(self.url)
#         self.assertEqual(view.func.__name__, views.SignUpView.as_view().__name__)


class SignUpPageTest(TestCase):

    username = "TestUser"
    email = "TestUser@email.com"

    def setUp(self):
        self.url = reverse("account_signup")
        self.response = self.client.get(self.url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi I am not here.")

    def test_signup_form(self):
        User = get_user_model()
        User.objects.create_user(self.username, self.email)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.all()[0].username, self.username)
        self.assertEqual(User.objects.all()[0].email, self.email)
