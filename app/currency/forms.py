from django import forms
from .models import Source, ContactUs, Rate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = '__all__'


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = '__all__'


User = get_user_model()


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
