from django import forms
from .models import Source, ContactUs, Rate


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
