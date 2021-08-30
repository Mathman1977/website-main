from django.contrib import admin
from .models import Reeks, Opgave, Oefening


class ChoiceInline(admin.TabularInline):
    model = Opgave
    extra = 3


@admin.register(Reeks)
class ReeksAdmin(admin.ModelAdmin):
    fieldsets = [
        ('reeksoverzicht',{'fields': ['titel','foto','uitleg',
            'datum','soort','glob_moeilkhgr','glob_strtijd',
            'vereiste_level','nodig_materiaal']}
            )
        ]
    #     ( 'date info', {'fields': ['onderwerp'], 'classes': ['collapse']}),
    # ]
    inlines = [ChoiceInline]
    search_fields = ['titel']
    list_display = ('titel', 'datum','glob_strtijd')

@admin.register(Oefening)
class OefeningAdmin(admin.ModelAdmin):
    search_fields = ['student']
    list_display = ('student','oef_datum')
