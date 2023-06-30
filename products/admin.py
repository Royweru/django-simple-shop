from django.contrib import admin

from .models import items

class ItemsAdmin(admin.ModelAdmin):
    list_display =('name','price','image','description')


admin.site.register(items,ItemsAdmin)
