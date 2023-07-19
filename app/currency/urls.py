from django.urls import path
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
)

app_name = 'currency'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('rates/', RateListView.as_view(), name='rate_list'),
    path('rates/create/', RateCreateView.as_view(), name='rate_create'),
    path('rates/update/<int:pk>/', RateUpdateView.as_view(), name='rate_update'),
    path('rates/details/<int:pk>/', RateDetailView.as_view(), name='rate_details'),
    path('rates/delete/<int:pk>/', RateDeleteView.as_view(), name='rate_delete'),
    path('contactus/', ContactUsListView.as_view(), name='contactus_list'),
    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus_create'),
    path('contactus/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contactus_update'),
    path('contactus/details/<int:pk>/', ContactUsDetailView.as_view(), name='contactus_details'),
    path('contactus/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contactus_delete'),
    path('source/', SourceListView.as_view(), name='source_list'),
    path('source/create/', SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source_update'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source_details'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source_delete'),
]
