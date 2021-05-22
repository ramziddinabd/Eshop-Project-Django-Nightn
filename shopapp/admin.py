from django.contrib import admin
from .models import Product, Contact, Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price','created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'price','created_at')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','phone')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'phone', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)

