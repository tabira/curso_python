from django.contrib import admin
from . import models

# Register your models here.




@admin.register(models.Reserva)
class ReservaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['cliente']


class ReservaInLine(admin.TabularInline):
    model = models.Reserva
    extra = 0


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'email', 'telefone']
    inlines = [ReservaInLine]
    date_hierarchy = 'registrado_em'
    list_filter = ['registrado_em']
    list_display = ['nome', 'email', 'registro_antigo']
    # fields = [
    #     'nome',
    #     'email',
    #     'telefone',
    #     'endereco',
    #     'registrado_em'
    # ]

    fieldsets = [
        (
            'Iformações básicas', {'fields': [
                'nome',
                'email',
                'telefone',
                'endereco'
            ]},

        ),
        ('Datas', {'fields': ['registrado_em']
                   # ,'classes':['collapse']
                   })
    ]
