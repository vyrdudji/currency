from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegisterView, UserActivateView

app_name = 'account'

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('activate/<slug:uidb64>/<slug:token>/', UserActivateView.as_view(), name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
