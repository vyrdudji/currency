from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from .views import (
    IndexView,
    RateListView,
    RateCreateView,
    RateUpdateView,
    RateDetailView,
    RateDeleteView,
    ContactUsListView,
    ContactUsCreateView,
    ContactUsUpdateView,
    ContactUsDetailView,
    ContactUsDeleteView,
    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    SourceDetailView,
    SourceDeleteView,
    CustomPasswordChangeView,
    CustomPasswordChangeDoneView,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
)

app_name = 'currency'

def logout_view(request):
    logout(request)
    return redirect('currency:index')

# Створення маршрутізатора та реєстрація ViewSets
router = DefaultRouter()
router.register(r'sources', SourceViewSet)
router.register(r'contactus', ContactUsViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    # Rates URLs
    path('rates/', RateListView.as_view(), name='rate_list'),
    path('rates/create/', RateCreateView.as_view(), name='rate_create'),
    path('rates/update/<int:pk>/', RateUpdateView.as_view(), name='rate_update'),
    path('rates/details/<int:pk>/', RateDetailView.as_view(), name='rate_details'),
    path('rates/delete/<int:pk>/', RateDeleteView.as_view(), name='rate_delete'),

    # ContactUs URLs
    path('contactus/', ContactUsListView.as_view(), name='contactus_list'),
    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus_create'),
    path('contactus/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contactus_update'),
    path('contactus/details/<int:pk>/', ContactUsDetailView.as_view(), name='contactus_details'),
    path('contactus/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contactus_delete'),

    # Source URLs
    path('source/', SourceListView.as_view(), name='source_list'),
    path('source/create/', SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source_update'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source_details'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source_delete'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',
         CustomPasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # API URLs
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
