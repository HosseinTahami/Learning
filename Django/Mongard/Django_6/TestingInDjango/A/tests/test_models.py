from django.test import TestCase
from A.models import Writer


class TestWriter(TestCase):
    def test_model_writer(self):
        writer = Writer.objects.create(
            name="test_writer", age=10, country="test_country", email="test_email"
        )

        self.assertEquals(str(writer), "test_writer || test_email")
