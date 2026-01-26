


from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'posted_date', 'published')  # 在列表顯示的欄位
    list_filter = ('location', 'published')  # 篩選器
    search_fields = ('title', 'description')  # 搜尋欄位


class JobAdmin(ImportExportModelAdmin):
    list_display = ('title', 'location', 'posted_date', 'published')  # 在列表顯示的欄位
    list_filter = ('location', 'published')  # 篩選器
    search_fields = ('title', 'description')  # 搜尋欄位
# 使用自訂的 JobAdmin
admin.site.register(Job, JobAdmin)
  



