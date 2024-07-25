from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book, Review



class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.user = get_user_model().objects.create_user(
            username="reviewer",
            email="reviewer@email.com",
            password="secret123",
        )

        cls.special_permission = Permission.objects.get(
            codename="special_status",
        )

        cls.book = Book.objects.create(
            title="Test Title",
            author="Test Author",
            price="25.00",
        )

        cls.review = Review.objects.create(
            title="Test Title",
            book=cls.book,
            author=cls.user,
            review="Test Review",
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Test Title")
        self.assertEqual(f"{self.book.author}", "Test Author")
        self.assertEqual(f"{self.book.price}", "25.00")

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email="reviewer@email.com", password="secret123")
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Title")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "%s?next=/books/" % (reverse("account_login")))
        response = self.client.get("%s?next=/books/" % (reverse("account_login")))
        self.assertTemplateUsed(response, "account/login.html")

    def test_book_detail_view_with_permissions(self):
        self.client.login(email="reviewer@email.com", password="secret123")
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test Author")
        self.assertTemplateUsed(response, "books/book_detail.html")
        self.assertContains(response, "Test Review")
