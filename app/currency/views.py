from django.shortcuts import render
from django.http.response import HttpResponse
from .models import ContactUs, Rate


def hello_world(request):
    return HttpResponse('Hello world!')


def rate_list(request):
    '''
    MVTU
    V - view
    U - urls
    M - model
    T - template
    '''
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }
    return render(request, 'rate_list.html', context)


def contact_us_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'contactus_list.html', {'contacts': contacts})
