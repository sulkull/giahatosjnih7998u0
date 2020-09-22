from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from sanpham.models import *

class THAdmin(admin.ModelAdmin):
    list_display = ['ten']
    search_fields = ['ten']
    list_per_page = 20
admin.site.register(thuonghieu,THAdmin)


class SP(resources.ModelResource):
    class Meta:
        model = sanpham
        # exclude = ('khosp_id',)
        fields = ('id', 'ten','masp','thuonghieusp','giabanle')
class SPAdmin(ImportExportModelAdmin):
    list_display = ['ten', 'masp', 'thuonghieusp', 'giabanle']
    list_filter = [ 'thuonghieusp']
    search_fields = ['ten', 'masp']
    # exclude = ('khosp_id',)
    list_per_page = 20
    resource_class = SP

admin.site.register(sanpham, SPAdmin)


