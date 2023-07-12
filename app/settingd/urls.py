"""
URL configuration for settingd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from currency.views import hello_world, rate_list, contact_us_list, source_list
from currency import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('rate/list/', rate_list),
    path('rate/create/', views.rate_create, name='rate_create'),
    path('contactus/list/', contact_us_list, name='contactus_list'),
    path('contactus/create/', views.contactus_create, name='contactus_create'),
    path('source/list/', source_list, name='source_list'),
    path('source/create/', views.source_create, name='source_create'),
    path('source/<int:pk>/', views.source_details, name='source_details'),
    path('source/update/<int:pk>/', views.source_update, name='source_update'),  # Add this line
    path('source/delete/<int:pk>/', views.source_delete, name='source_delete'),
]

