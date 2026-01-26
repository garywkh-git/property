from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Salesperson

# Register your models here.
class SalespersonAdmin(admin.ModelAdmin):
    list_display = ('name','description','phone','email','hire_date','is_mvp') #tuple
    # list_display_links = ('name','email') #tuple
    list_editable = ('is_mvp',) #tuple
    #list_fields = 'name', #tuple
    search_fields = ('name',) #tuple
    list_per_page = 25



class SalespersonAdmin(ImportExportModelAdmin):
    list_display = ('name','description','phone','email','hire_date','is_mvp') #tuple
    # list_display_links = ('name','email') #tuple
    list_editable = ('is_mvp',) #tuple
    search_fields = ('name',) #tuple
    list_per_page = 25
    



admin.site.register(Salesperson, SalespersonAdmin)