from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Cliente)
class ClienteSite(admin.ModelAdmin):
    search_fields = ['nome']
    list_filter = ['registro']
    list_display = ['nome', 'email', 'genero', 'registro_antigo']
    fieldsets = [
        (
            None, {'fields': [
                'nome',
                'endereco',
                'telefone',
                'email',
                'genero'

            ]},

        ),
        ('documetnos', {'fields': ['cpf']
            , 'classes': ['collapse']
                        })
    ]


class DoadorSite(admin.ModelAdmin):
    search_fields = ['nome']
    list_filter = ['registro']
    list_display = ['nome', 'email', 'genero', 'registro_antigo']
    fieldsets = [
        (
            None, {'fields': [
                'nome',
                'endereco',
                'telefone',
                'email',
                'genero'

            ]},

        ),
        ('documetnos', {'fields': ['cpf']
            , 'classes': ['collapse']
                        })
    ]


class AnimalInline(admin.TabularInline):
    model = models.Animal


class RacaSite(admin.ModelAdmin):
    inlines = [AnimalInline]
    search_fields = ['nome']
    list_filter = ['porte']
    list_display = ['nome', 'porte']


class AnimalSite(admin.ModelAdmin):
    list_display = ['nome', 'especie', 'raca_str']
    list_filter = ['raca']
    search_fields = ['nome']

    def raca_str(self, linha):
        return linha.raca.nome


class AdocaoSite(admin.ModelAdmin):
    search_fields = ['animal__nome', 'cliente__nome']
    list_filter = ['registro']


admin.site.register(models.Adocao, AdocaoSite)
admin.site.register(models.Animal, AnimalSite)
admin.site.register(models.Doador, DoadorSite)
admin.site.register(models.Raca, RacaSite)
