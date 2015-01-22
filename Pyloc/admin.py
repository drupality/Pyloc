from django.contrib import admin
from Pyloc.models import Venue, VenueCategory

class VenueCategoryAdmin(admin.ModelAdmin):
    pass


class VenueAdmin(admin.ModelAdmin):
    exclude = ['longitude', 'latitude']

    filter_horizontal = ('categories',)

    fieldsets = [
        (None, {'fields': ['name', 'city', 'address']}),
        (None, {'fields': ['categories']}),
    ]


admin.site.register(Venue, VenueAdmin)
admin.site.register(VenueCategory, VenueCategoryAdmin)
