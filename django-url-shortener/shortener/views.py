import re
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from django.views.generic import ListView
from shortener.models import ShortenedURL
from .helper import shortened_url_generator
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class MyURLsView(LoginRequiredMixin, ListView):
    model = ShortenedURL
    template_name = 'urls_list.html'
    context_object_name = 'urls_list'
    paginate_by = 6

    # def get_queryset(self):
    #     object_length = len(ShortenedURL.objects.filter(user=self.request.user))
    #     return [ShortenedURL.objects.filter(user=self.request.user).order_by('-created_at'), object_length]



# def urls_list(request):
#     object_list = ShortenedURL.objects.get(user=request.)
#     paginator = Paginator(object_list, 6)
#     page = request.GET.get('page')
#     try:
#         urls = paginator.page(page)
#     except PageNotAnInteger:
#         urls = paginator.page(1)
#     except EmptyPage:
#         urls = paginator.page(paginator.num_pages)
#     return render(request, 'urls_list.html', {'page': page, 'urls': urls})


def index(request):
    context = {}
    context.update(csrf(request))
    return render(request, 'home.html', context)


def redirect_to_original_url(request, short_url):
    url = get_object_or_404(ShortenedURL, pk=short_url)
    url.count += 1
    url.save()
    return redirect(url.original_url)


def url_pattern(url):
    pattern = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    result = bool(re.match(pattern, url))
    return result


def get_shortened_url(request):
    url = request.POST.get("url", "")
    if url_pattern(url):
        if not (url is None or url == '') and request.user.is_authenticated:
            try:
                current_url = ShortenedURL.objects.get(original_url__exact=url, user_id__exact=request.user.pk)
                short_url = current_url.short_url
            except ShortenedURL.DoesNotExist:
                short_url = shortened_url_generator()
                result = ShortenedURL(original_url=url, short_url=short_url, user_id=request.user.pk)
                result.save()
            response = {'url': short_url}
            return JsonResponse(response)
    else:
        return JsonResponse({'error': 'This page could not be loaded.'})
    return JsonResponse({'error': 'This page could not be loaded.'})
