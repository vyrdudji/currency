from django.urls import path
from .views import (
    IndexView,
    RateListView,
    ContactUsListView,
    SourceListView,
    ContactUsCreateView,
    RateCreateView,
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,
    SourceDetailsView,
    RateUpdateView,
    RateDeleteView,
    RateDetailsView,
    ContactUsUpdateView,
    ContactUsDeleteView,
    ContactUsDetailsView,
)

app_name = 'currency'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('rate/list/', RateListView.as_view(), name='rate_list'),
    path('rate/create/', RateCreateView.as_view(), name='rate_create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate_update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate_delete'),
    path('rate/details/<int:pk>/', RateDetailsView.as_view(), name='rate_details'),
    path('contactus/list/', ContactUsListView.as_view(), name='contactus_list'),
    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus_create'),
    path('contactus/update/<int:pk>/', ContactUsUpdateView.as_view(), name='contactus_update'),
    path('contactus/delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contactus_delete'),
    path('contactus/details/<int:pk>/', ContactUsDetailsView.as_view(), name='contactus_details'),
    path('source/list/', SourceListView.as_view(), name='source_list'),
    path('source/create/', SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source_update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source_delete'),
    path('source/details/<int:pk>/', SourceDetailsView.as_view(), name='source_details'),
]
