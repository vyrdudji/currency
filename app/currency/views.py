from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactUs, Rate, Source
from .forms import ContactUsForm, SourceForm, RateForm


def hello_world(request):
    return HttpResponse('Hello world!')


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }
    return render(request, 'rate_list.html', context)


def contact_us_list(request):
    contacts = ContactUs.objects.all()
    return render(request, 'contactus_list.html', {'contacts': contacts})


def source_list(request):
    sources = Source.objects.all()
    source_form = SourceForm()
    context = {
        'sources': sources,
        'source_form': source_form,
    }
    return render(request, 'source_list.html', context)


def contactus_create(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactus_list')
    else:
        form = ContactUsForm()
    return render(request, 'contactus_create.html', {'form': form})


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rate_list')
    else:
        form = RateForm()
    return render(request, 'rate_create.html', {'form': form})


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('source_list')
    else:
        form = SourceForm()
    context = {
        'source_form': form,
    }
    return render(request, 'source_create.html', context)


def source_update(request, pk):
    source = Source.objects.get(pk=pk)
    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return redirect('source_list')
    else:
        form = SourceForm(instance=source)
    context = {
        'source_form': form,
        'source': source,
    }
    return render(request, 'source_update.html', context)


def source_delete(request, pk):
    source = Source.objects.get(pk=pk)
    if request.method == 'POST':
        source.delete()
        return redirect('source_list')
    context = {
        'source': source,
    }
    return render(request, 'source_delete.html', context)


def source_details(request, pk):
    source = Source.objects.get(pk=pk)
    context = {
        'source': source,
    }
    return render(request, 'source_details.html', context)
