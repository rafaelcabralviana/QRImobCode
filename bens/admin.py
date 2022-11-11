from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from .models import Category, Product

admin.site.site_header = 'PATRIMÔNIO EDIÇÕES ADMIN'
admin.site.site_title = 'PATRIMÔNIO EDIÇÕES'


class PropertyAdminResource(resources.ModelResource):

    class Meta:
        model = Product
        import_id_fields = ("codigo",)
        skip_unchanged = True
        report_skipped = True
        
        fields = ["categoria", "codigo", "local", "setor", "tag", "descricao", "responsavel", "data_inicial", "data_final"]
        
        exclude = ("id", "created", "modified", "slug", "image", "is_available", )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","id"]
    
    
    


@admin.register(Product)
#import_export + ADMIN
class TestappImportExport(ImportExportModelAdmin):
    resource_class = PropertyAdminResource
    list_display = ["codigo", "slug", "descricao", "categoria", "local", "setor", "image"]
    search_fields = ["codigo"]
    pass
    #resource_class = PropertyAdminResource

