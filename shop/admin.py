from django.contrib import admin
from .models import Product, Category, Sale, Brand, ProductColor, Applications
from django.utils.safestring import mark_safe




class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'created_at', 'updated_at')
    list_filter = ('name','created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'created_at', 'updated_at')
    list_filter = ('name','category','created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')





class ProductAdmin(admin.ModelAdmin):

    list_display = ('id','category', 'brand', 'name', 'price', 'image', 'description', 'color', 'lte_exists', 'created_at', 'updated_at', )
    list_filter = ('category','lte_exists', 'created_at', 'updated_at')
    search_fields = ('name', 'category', 'price', 'created_at', 'updated_at')

    def image_show(self, obj):
        if obj.image:
            return mark_safe(f'<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}" width="50" height="60"></a>')
        else:
            return '-'



class SaleAdmin(admin.ModelAdmin):
    list_display = ('id','shop', 'name', 'description', 'start_date', 'end_date', 'image', )
    list_filter = ('shop','start_date', 'end_date')
    search_fields = ('shop', 'name', 'description', 'start_date', 'end_date', 'image', )
    


class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'created_at', 'updated_at', )
    list_filter = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')

class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id','shop', 'name', 'phone', 'whatsapp', 'message', 'created_at', 'updated_at', )
    list_filter = ('created_at', 'updated_at', )




admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Applications,ApplicationsAdmin)
admin.site.register(Sale,SaleAdmin)
admin.site.register(ProductColor,ProductColorAdmin)




