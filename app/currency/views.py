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
    # PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from .forms import CustomPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages


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


class RateUpdateView(UserPassesTestMixin, UpdateView):
    login_url = reverse_lazy('currency:login')
    model = Rate
    form_class = RateForm
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate_list')

    def test_func(self):
        return self.request.user.is_superuser


class RateDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('currency:login')
    model = Rate
    template_name = 'rate_details.html'
    context_object_name = 'rate'


class RateDeleteView(UserPassesTestMixin, DeleteView):
    login_url = reverse_lazy('currency:login')
    model = Rate
    template_name = 'rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')

    def test_func(self):
        return self.request.user.is_superuser


class ContactUsListView(ListView):
    model = ContactUs
    template_name = 'contactus_list.html'
    context_object_name = 'contacts'


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


class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('currency:password_reset_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocol'] = 'http'  # або 'https', залежно від веб-сайту
        return context


class CustomPasswordChangeView(UserPassesTestMixin, LoginRequiredMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('custom_password_change_done')  # Updated

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
    # success_url = reverse_lazy('custom_password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
