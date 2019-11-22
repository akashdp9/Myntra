from django.contrib import admin
# Register your models here.
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','type', 'image','brand',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('quantity','total_price','item','is_cancelled',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Order,OrderAdmin)
