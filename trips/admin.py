from django.contrib import admin

from .models import Trip, TourAuthor, RoadMap, Registration


class AdminRoadMap(admin.StackedInline):
    model = RoadMap


class AdminTrip(admin.ModelAdmin):
    fieldsets = [
        ('Шапка', {'fields': ['owner', 'img_trip', 'title', 'description']}),
        ('Даты, Стоимость и колличество участников', {'fields': ['price', ('date_start', 'date_end'), 'number_party']}),
        ('Включено / не включено в стоимость', {'fields': ['included_coast', 'not_included_coast']}),
        # ('Служебное поле', {'fields': ['slug']})
    ]
    inlines = [
        AdminRoadMap,
    ]

    # fields = ('owner', 'img_trip', 'title', 'description', 'price', ('date_start', 'date_end'), 'included_coast',
    #           'not_included_coast', 'number_party')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(AdminTrip, self).get_form(request, obj, **kwargs)
        form.base_fields['price'].widget.attrs['style'] = 'width: 20em;'
        return form


admin.site.register(Trip, AdminTrip)
admin.site.register(TourAuthor)
admin.site.register(RoadMap)
admin.site.register(Registration)
