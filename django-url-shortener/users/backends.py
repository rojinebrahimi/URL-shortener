from django.contrib.auth.backends import BaseBackend

from .models import CustomUser


class EmailAuthenticationBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        email = kwargs['username'].lower()
        password = kwargs['password']
        try:
            custom_user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None
        else:
            if custom_user.is_active and custom_user.check_password(password):
                return custom_user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
