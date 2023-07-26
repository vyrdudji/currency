from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import View
from django.utils.http import urlsafe_base64_decode

from .forms import UserSignUpForm

User = get_user_model()


class RegisterView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('account:login')
    template_name = 'registration/register.html'


class UserActivateView(View):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')

        try:
            # decode uidb64 to user id
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)

            if default_token_generator.check_token(user, token):
                user.is_active = True
                if hasattr(user, 'profile'):
                    user.profile.email_confirmed = True
                user.save()
                return render(request, 'registration/activation.html', {'activated': True})

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            pass

        return render(request, 'registration/activation.html', {'activated': False})
