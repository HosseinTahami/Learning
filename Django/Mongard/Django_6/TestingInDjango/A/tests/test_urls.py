from django.test import SimpleTestCase
from django.urls import reverse, resolve
from A.views import Home, About


class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse("home:home")
        self.assertEquals(resolve(url).func.view_class, Home)

    def test_about(self):
        url = reverse("home:about", kwargs={"username": "hossein"})
        print(url)
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, About)
