from django.db.models import Count
from django import template
from users.models import CustomUser
from ..models import ShortenedURL

register = template.Library()


@register.simple_tag
def total_urls():
    print(ShortenedURL.objects.filter(user_id=CustomUser.pk).count())
