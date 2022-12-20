from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        )
    list_editable = (
        'new_building',
    )
    list_filter = (
        'new_building',
        'rooms_number',
        'active',
    )
    raw_id_fields = ('like',)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
