from django.contrib import admin
from .models import ShortenedURL


@admin.register(ShortenedURL)
class ShortenedAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_url', 'created_at', 'count')
    list_filter = ('user', 'created_at')
    search_fields = ('short_url', 'user')
