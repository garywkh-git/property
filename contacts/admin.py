from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'listing', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'listing', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)