from django.views.generic import (
    ListView, CreateView, UpdateView, DetailView,
    DeleteView, TemplateView
)
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .models import ContactUs, Rate, Source
from .forms import ContactUsForm, SourceForm, RateForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from .forms import CustomPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db.models import Q
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from .filters import RateFilter, ContactUsFilter, SourceFilter
from .serializers import ContactUsSerializer, SourceSerializer
import re

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class IndexView(TemplateView):
    template_name = 'index.html'


class CrispyFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', self.submit_label))
        return form


class RateListView(ListView):
    model = Rate
    template_name = 'rate_list.html'
    context_object_name = 'rates'
    paginate_by = 10

    def get_queryset(self):
        rates = Rate.objects.all().order_by('created')

        # Фільтрація
        self.filter = RateFilter(self.request.GET, queryset=rates)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter

        # Отримуємо параметри фільтрації, окрім 'page'
        context['filter_params'] = '&'.join(
            f'{key}={value}'
            for key, value in self.request.GET.items()
            if key != 'page'
        )
        return context


class RateCreateView(CrispyFormMixin, CreateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_create.html'
    success_url = reverse_lazy('currency:rate_list')
    submit_label = 'Create Rate'


class RateUpdateView(CrispyFormMixin, UserPassesTestMixin, UpdateView):
    login_url = reverse_lazy('currency:login')
    model = Rate
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate_list')
    submit_label = 'Update Rate'

    def test_func(self):
        return self.request.user.is_superuser


class RateDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('currency:login')
    model = Rate
    template_name = 'rate_details.html'
    context_object_name = 'rate'


class RateDeleteView(CrispyFormMixin, UserPassesTestMixin, DeleteView):
    login_url = reverse_lazy('currency:login')
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')
    submit_label = 'Delete Rate'

    def test_func(self):
        return self.request.user.is_superuser


class ContactUsListView(ListView):
    model = ContactUs
    template_name = 'contactus_list.html'
    context_object_name = 'contacts'
    paginate_by = 10

    def get_queryset(self):
        contacts = ContactUs.objects.all().order_by('id')

        # Фільтрація і сортування
        search_query = self.request.GET.get('search', '')
        if search_query:
            contacts = contacts.filter(Q(subject__icontains=search_query) | Q(message__icontains=search_query))

        self.filter = ContactUsFilter(self.request.GET, queryset=contacts)
        return self.filter.qs.order_by('-created_at')  # сортування за датою

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter

        # Отримуємо параметри фільтрації, окрім 'page'
        context['filter_params'] = '&'.join(
            f'{key}={value}'
            for key, value in self.request.GET.items()
            if key != 'page'
        )
        return context


class ContactUsCreateView(CrispyFormMixin, CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('currency:contactus_list')
    submit_label = 'Create Contact Us'

    def form_valid(self, form):
        response = super().form_valid(form)
        serializer = ContactUsSerializer(data=form.cleaned_data)
        if serializer.is_valid():
            serializer.save()
            messages.success(self.request, 'Контакт успішно створений.')
        else:
            # Виводимо помилки в консоль
            print("Serializer errors: ", serializer.errors)

            # Додаємо складнішу логіку обробки помилок
            error_messages = []
            for field, errors in serializer.errors.items():
                for error in errors:
                    error_messages.append(f"Поле {field}: {error}")

            for error_message in error_messages:
                messages.error(self.request, error_message)

        return response


class ContactUsUpdateView(CrispyFormMixin, UpdateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contactus_update.html'
    success_url = reverse_lazy('currency:contactus_list')
    submit_label = 'Update Contact Us'


class ContactUsDetailView(DetailView):
    model = ContactUs
    template_name = 'contactus_details.html'
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ContactUs.objects.all()
        return context


class ContactUsDeleteView(CrispyFormMixin, DeleteView):
    model = ContactUs
    template_name = 'contactus_delete.html'
    success_url = reverse_lazy('currency:contactus_list')
    submit_label = 'Delete Contact Us'


class SourceListView(ListView):
    model = Source
    template_name = 'source_list.html'
    context_object_name = 'sources'
    paginate_by = 10

    def get_queryset(self):
        sources = Source.objects.all().order_by('id')

        # Фільтрація
        self.filter = SourceFilter(self.request.GET, queryset=sources)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter

        # Отримуємо параметри фільтрації, окрім 'page'
        context['filter_params'] = '&'.join(
            f'{key}={value}'
            for key, value in self.request.GET.items()
            if key != 'page'
        )
        return context


class SourceCreateView(CrispyFormMixin, CreateView):
    model = Source
    form_class = SourceForm
    template_name = 'source_create.html'
    success_url = reverse_lazy('currency:source_list')
    submit_label = 'Create Source'


class SourceUpdateView(CrispyFormMixin, UpdateView):
    model = Source
    form_class = SourceForm
    template_name = 'source_update.html'
    success_url = reverse_lazy('currency:source_list')
    submit_label = 'Update Source'


class SourceDetailView(DetailView):
    model = Source
    template_name = 'source_details.html'
    context_object_name = 'source'


class SourceDeleteView(CrispyFormMixin, DeleteView):
    model = Source
    template_name = 'source_delete.html'
    success_url = reverse_lazy('currency:source_list')
    submit_label = 'Delete Source'


class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('currency:password_reset_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocol'] = 'http'
        return context


class CustomPasswordChangeView(UserPassesTestMixin, LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('custom_password_change_done')

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Пароль успішно змінено.')
        return response


class CustomPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'


@receiver(pre_save, sender=User)
def clean_user_phone_number(sender, instance, **kwargs):
    if hasattr(instance, 'phone') and instance.phone:
        instance.phone = re.sub(r'\D', '', instance.phone)


@api_view(['POST'])
def contact_us_api(request):
    if request.method == 'POST':
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
