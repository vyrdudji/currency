from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('currency.urls')),
    path('account/', include('account.urls', namespace='account')),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
