from django.test import SimpleTestCase
from django.urls import reverse, resolve

from . import views


class HomePageTest(SimpleTestCase):

    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Home Page")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "I am not here !")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, views.HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        self.url = reverse("about")
        self.response = self.client.get(self.url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "About Page")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "I am not here !")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, views.AboutPageView.as_view().__name__)
