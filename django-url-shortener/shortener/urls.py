from django.urls import path
from . import views
from .views import MyURLsView

urlpatterns = [
    path('', views.index, name='home'),
    #path('myurls/', views.urls_list, name='urls_list'),
    path('myurls/', MyURLsView.as_view(), name='urls_list'),
    path('<short_url>', views.redirect_to_original_url, name='redirect_to_original'),
    path('shortened/', views.get_shortened_url, name='shortened_url'),
]
