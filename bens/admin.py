from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from .models import Category, Product

admin.site.site_header = 'PATRIMÔNIO EDIÇÕES ADMIN'
admin.site.site_title = 'PATRIMÔNIO EDIÇÕES'

class PropertyAdminResource(resources.ModelResource):

    class Meta:
        model = Product
        import_id_fields = ["codbem", "local", "setor", "tag", "descricao", ]
        exclude = ("id", "created", "modified", "slug", "image", "is_available", )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","id"]
    
    
    


@admin.register(Product)
#import_export + ADMIN
class TestappImportExport(ImportExportModelAdmin):
    resource_class = PropertyAdminResource
    list_display = ["codbem", "descricao", "categoria", "local", "image"]
    search_fields = ["codbem"]
    pass
    #resource_class = PropertyAdminResource

