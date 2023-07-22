# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Rate, ContactUs, Source


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in ContactUs._meta.get_fields()]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Rate)
admin.site.register(Source)
