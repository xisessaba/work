from django.contrib import admin
from .models import Product,Users, Category, Sale
from django.utils.safestring import mark_safe

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'email', 'phone', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'address', 'created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'created_at', 'updated_at')
    list_filter = ('name','created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'price', 'image_show', 'description', 'lte_exists', 'created_at', 'updated_at')
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
    





admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Users,UsersAdmin)
admin.site.register(Sale,SaleAdmin)



