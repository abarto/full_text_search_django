from django.contrib import admin

from .models import Item, Part


class PartInline(admin.TabularInline):
    model = Part


class ItemAdmin(admin.ModelAdmin):
    inlines = (PartInline,)


admin.site.register(Item, ItemAdmin)
admin.site.register(Part)
