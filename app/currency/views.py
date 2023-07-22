from django.views.generic import (
    ListView, CreateView, UpdateView, DetailView,
    DeleteView, TemplateView
)
from django.urls import reverse_lazy
from .models import ContactUs, Rate, Source
from .forms import ContactUsForm, SourceForm, RateForm
from django.core.mail import send_mail
from django.conf import settings


class IndexView(TemplateView):
    template_name = 'index.html'


class RateListView(ListView):
    model = Rate
    template_name = 'rate_list.html'
    context_object_name = 'rates'


class RateCreateView(CreateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate_list')


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate_list')


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_details.html'
    context_object_name = 'rate'


class RateDeleteView(DeleteView):
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')


class ContactUsListView(ListView):
    model = ContactUs
    template_name = 'contactus_list.html'
    context_object_name = 'contacts'


# class ContactUsCreateView(CreateView):
#     model = ContactUs
#     form_class = ContactUsForm
#     template_name = 'contactus_create.html'
#     success_url = reverse_lazy('currency:contactus_list')
#     http_method_names = ['get', 'post']
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

class ContactUsCreateView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('currency:contactus_list')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Відправлення електронної пошти
        subject = 'Нове повідомлення з форми зворотного звʼязку'
        message = f'Від: {form.instance.email_from}\n' \
                  f'Тема: {form.instance.subject}\n' \
                  f'Повідомлення: {form.instance.message}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['vyrdudji7@gmail.com']  # Ваша адреса електронної пошти

        send_mail(subject, message, from_email, recipient_list)

        return response


class ContactUsUpdateView(UpdateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contactus_update.html'
    success_url = reverse_lazy('currency:contactus_list')


class ContactUsDetailView(DetailView):
    model = ContactUs
    template_name = 'contactus_details.html'
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ContactUs.objects.all()
        return context


class ContactUsDeleteView(DeleteView):
    model = ContactUs
    template_name = 'contactus_delete.html'
    success_url = reverse_lazy('currency:contactus_list')


class SourceListView(ListView):
    model = Source
    template_name = 'source_list.html'
    context_object_name = 'sources'


class SourceCreateView(CreateView):
    model = Source
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source_list')


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:source_list')


class SourceDetailView(DetailView):
    model = Source
    template_name = 'source_details.html'
    context_object_name = 'source'


class SourceDeleteView(DeleteView):
    model = Source
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source_list')
