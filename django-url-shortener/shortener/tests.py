from django.test import TestCase
from .models import ShortenedURL, CustomUser


class ShortenedURLTestCase(TestCase):
    def setUp(self):
        user = CustomUser.username
        ShortenedURL.objects.create(user=user,
                                    original_url="https://docs.djangoproject.com/en/3.0/topics/testing/overview/", short_url='QQQ1234567')

        ShortenedURL.objects.create(user=user, original_url="https://docs.djangoproject.com/en/3.0/topics/testing/", short_url='poi0987654')

        def test_short_url(self):
            url_one = ShortenedURL.objects.get(
                original_url="https://docs.djangoproject.com/en/3.0/topics/testing/overview/")
            url_two = ShortenedURL.objects.get(original_url='https://docs.djangoproject.com/en/3.0/topics/testing/')
            self.assertEqual(url_one.short_url, 'QQQ1234567')
            self.assertEqual(url_two.short_url, 'poi0987654')