from django.shortcuts import render
from django.http.response import HttpResponse
from .models import ContactUs


def hello_world(request):
    return HttpResponse('Hello world!')


def contact_us_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'contactus_list.html', {'contacts': contacts})
