from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.core.mail import send_mail
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


send_mail('Password Reset', 'Click the link to reset your password', 'from@example.com', ['to@example.com'],
          fail_silently=False)
