from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls) :
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    # def test_url_available_by_name(self):
    #     response = self.client.get(reverse("home"))
    #     self.assertEqual(response.status_code, 200)

    # def test_template_name_correct(self):
    #     response = self.client.get(reverse("home"))
    #     self.assertTemplateUsed(response, "home.html")
    
    # def test_template_content(self):
    #     response = self.client.get(reverse("home"))
    #     self.assertContains(response, "This is a test!")

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")
        self.assertTemplateUsed(response, "home.html")
        self.assertEqual(response.status_code, 200)