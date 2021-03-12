import string, random

from shortener.models import ShortenedURL


def shortened_url_generator():
    size = 10
    chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(chars) for _ in range(size))
    while True:
        try:
            temp = ShortenedURL.objects.get(pk=short_url)
            return temp
        except ShortenedURL.DoesNotExist:
            return short_url
