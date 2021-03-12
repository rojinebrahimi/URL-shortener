from django.db import models
from django.urls import reverse
from django.utils import timezone
from Url_Shortener import settings
from users.models import CustomUser

#
# class PersonalUrlManager(models.Manager):
#     class Meta:
#         user = CustomUser.pk
#
#     def get_queryset(self, user):
#         return super(PersonalUrlManager, self).get_queryset().filter(user=self.user.primary_key)


class ShortenedURL(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    original_url = models.CharField(max_length=2048, null=False)
    short_url = models.CharField(max_length=10, unique=True, blank=True, primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    count = models.PositiveIntegerField(default=0)
    # personal_url = PersonalUrlManager()
    # objects = models.Manager()

    def __str__(self):
        return self.original_url

    def get_absolute_url(self):
        return reverse('home')
