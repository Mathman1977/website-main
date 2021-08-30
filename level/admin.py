from django.contrib import admin
from .models import OpgavenReeks, Opgave,Excercice


class ChoiceInline(admin.TabularInline):
    model = Opgave
    extra = 3


@admin.register(OpgavenReeks)
class OpgavenReeksAdmin(admin.ModelAdmin):
    fieldsets = [
        ('reeksoverzicht',{'fields': ['titel','foto','uitleg','soort','onderwerp','glob_moeilkhgr','glob_strtijd',
            'vereiste_level','nodig_materiaal','joke','website_url']}
            )
            # ,
            # ( 'date info', {'fields': ['onderwerp'], 'classes': ['collapse']}),
            ]
    inlines = [ChoiceInline]
    search_fields = ['titel']
    list_display = ('titel', 'datum','glob_strtijd') # # opgaven



@admin.register(Excercice)
class OefeningAdmin(admin.ModelAdmin):
    search_fields = ['player']
    list_display = ('oef_datum','player','opgave','jouw_antwoord','juist_fout','snelheid','jouw_delta')
