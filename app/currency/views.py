from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .models import ContactUs, Rate, Source
from .forms import ContactUsForm, SourceForm, RateForm


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class RateListView(View):
    def get(self, request):
        rates = Rate.objects.all()
        context = {
            'rates': rates
        }
        return render(request, 'rate_list.html', context)


class RateCreateView(View):
    def get(self, request):
        form = RateForm()
        return render(request, 'rate_create.html', {'form': form})

    def post(self, request):
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('currency:rate_list'))
        return render(request, 'rate_create.html', {'form': form})


class RateUpdateView(View):
    def get(self, request, pk):
        rate = get_object_or_404(Rate, pk=pk)
        form = RateForm(instance=rate)
        context = {
            'form': form,
            'rate': rate,
        }
        return render(request, 'rate_update.html', context)

    def post(self, request, pk):
        rate = get_object_or_404(Rate, pk=pk)
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return redirect(reverse('currency:rate_list'))
        context = {
            'form': form,
            'rate': rate,
        }
        return render(request, 'rate_update.html', context)


class RateDeleteView(View):
    def get(self, request, pk):
        rate = get_object_or_404(Rate, pk=pk)
        context = {
            'rate': rate,
        }
        return render(request, 'rate_delete.html', context)

    def post(self, request, pk):
        rate = get_object_or_404(Rate, pk=pk)
        rate.delete()
        return redirect(reverse('currency:rate_list'))


class RateDetailsView(View):
    def get(self, request, pk):
        rate = get_object_or_404(Rate, pk=pk)
        context = {
            'rate': rate,
        }
        return render(request, 'rate_details.html', context)


class ContactUsListView(View):
    def get(self, request):
        contacts = ContactUs.objects.all()
        return render(request, 'contactus_list.html', {'contacts': contacts})


class ContactUsCreateView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, 'contactus_create.html', {'form': form})

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('currency:contactus_list'))
        return render(request, 'contactus_create.html', {'form': form})


class ContactUsUpdateView(View):
    def get(self, request, pk):
        contact = get_object_or_404(ContactUs, pk=pk)
        form = ContactUsForm(instance=contact)
        context = {
            'form': form,
            'contact': contact,
        }
        return render(request, 'contactus_update.html', context)

    def post(self, request, pk):
        contact = get_object_or_404(ContactUs, pk=pk)
        form = ContactUsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(reverse('currency:contactus_list'))
        context = {
            'form': form,
            'contact': contact,
        }
        return render(request, 'contactus_update.html', context)


class ContactUsDeleteView(View):
    def get(self, request, pk):
        contact = get_object_or_404(ContactUs, pk=pk)
        context = {
            'contact': contact,
        }
        return render(request, 'contactus_delete.html', context)

    def post(self, request, pk):
        contact = get_object_or_404(ContactUs, pk=pk)
        contact.delete()
        return redirect(reverse('currency:contactus_list'))


class ContactUsDetailsView(View):
    def get(self, request, pk):
        contact = get_object_or_404(ContactUs, pk=pk)
        context = {
            'contact': contact,
        }
        return render(request, 'contactus_details.html', context)


class SourceListView(View):
    def get(self, request):
        sources = Source.objects.all()
        source_form = SourceForm()
        context = {
            'sources': sources,
            'source_form': source_form,
        }
        return render(request, 'source_list.html', context)


class SourceCreateView(View):
    def get(self, request):
        form = SourceForm()
        return render(request, 'source_create.html', {'source_form': form})

    def post(self, request):
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('currency:source_list'))
        return render(request, 'source_create.html', {'source_form': form})


class SourceUpdateView(View):
    def get(self, request, pk):
        source = get_object_or_404(Source, pk=pk)
        form = SourceForm(instance=source)
        context = {
            'source_form': form,
            'source': source,
        }
        return render(request, 'source_update.html', context)

    def post(self, request, pk):
        source = get_object_or_404(Source, pk=pk)
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return redirect(reverse('currency:source_list'))
        context = {
            'source_form': form,
            'source': source,
        }
        return render(request, 'source_update.html', context)


class SourceDeleteView(View):
    def get(self, request, pk):
        source = get_object_or_404(Source, pk=pk)
        context = {
            'source': source,
        }
        return render(request, 'source_delete.html', context)

    def post(self, request, pk):
        source = get_object_or_404(Source, pk=pk)
        source.delete()
        return redirect(reverse('currency:source_list'))


class SourceDetailsView(View):
    def get(self, request, pk):
        source = get_object_or_404(Source, pk=pk)
        context = {
            'source': source,
        }
        return render(request, 'source_details.html', context)