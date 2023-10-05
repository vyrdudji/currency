from rest_framework import serializers
from .models import Source, ContactUs
from django.core.mail import send_mail
from decouple import config


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

    def create(self, validated_data):
        # Логіка відправки електронного листа
        subject = validated_data.get('subject', 'Message from my project')
        message = validated_data.get('message', '')
        from_email = config('EMAIL_HOST_USER')
        # recipient_list = ['recipient@example.com']  # Замініть на електронну адресу отримувача
        recipient_list = [from_email]

        send_mail(subject, message, from_email, recipient_list)

        return ContactUs.objects.create(**validated_data)
