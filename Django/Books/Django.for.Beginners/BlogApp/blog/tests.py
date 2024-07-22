from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        cls.post = Post.objects.create(
            title="Test Title",
            body="Test Body",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "Test Title")
        self.assertEqual(self.post.body, "Test Body")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "Test Title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_createview(self):
        response = self.client.get("/post/new/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_updateview(self):
        response = self.client.get("/post/1/edit/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_deleteview(self):
        response = self.client.get("/post/1/delete/")
        self.assertEqual(response.status_code, 200)

    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Test Body")

    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/10000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "post_detail.html")
        self.assertContains(response, "Test Title")

    def test_post_createview(self):
        response = self.client.post(
            reverse("post_new"),
            {
                "title": "New Test Title",
                "body": "New Test Body",
                "author": self.user.id,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "New Test Title")
        self.assertEqual(Post.objects.last().body, "New Test Body")

    def test_post_updateview(self):
        response = self.client.post(
            reverse("post_edit", args="1"),
            {
                "title": "Update Test Title",
                "body": "Update Test Body",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Update Test Title")
        self.assertEqual(Post.objects.last().body, "Update Test Body")

    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
