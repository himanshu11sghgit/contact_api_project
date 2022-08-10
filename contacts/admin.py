from django.contrib import admin

from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'first_name', 'last_name', 'phone', 'country_code')