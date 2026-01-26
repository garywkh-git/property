# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import News

# @admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'salesperson', 'created_at')

class NewsAdmin(ImportExportModelAdmin):
    list_display = ('title', 'salesperson', 'created_at')

admin.site.register(News, NewsAdmin)