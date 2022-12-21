from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInstanceInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
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
    inlines = [
        OwnerInstanceInline,
        ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'pure_phone',)
    raw_id_fields = ('flats',)
