from django import forms
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


class UserSignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=15, required=False)
    username = forms.CharField(min_length=4, max_length=16, required=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
            'phone',
            'password1',
            'password2',
        )

    def clean(self):
        cleaned_data: dict = super().clean()

        if not self.errors:
            if cleaned_data['password1'] != cleaned_data['password2']:
                raise forms.ValidationError('Passwords should match!')

        return cleaned_data

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise forms.ValidationError('Phone number should contain only digits!')
        return phone

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_password(self.cleaned_data['password1'])
        instance.is_active = False
        if commit:
            instance.save()
            self._send_mail()
        return instance

    def _send_mail(self):
        token = default_token_generator.make_token(self.instance)
        uid = urlsafe_base64_encode(force_bytes(str(self.instance.pk)))
        url_path = reverse('account:activate', args=[uid, token])
        link = settings.HTTP_PROTOCOL + "://" + settings.DOMAIN + url_path

        send_mail(
            'Thanks for signing up!',
            f'Click the link to activate your account: {link}',
            settings.DEFAULT_FROM_EMAIL,
            [self.instance.email],
            fail_silently=False
        )
