from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Hospedagem)
class HospedagemAdmin(admin.ModelAdmin):
    list_display=('data_entrada', "data_saida","valor","cliente","quarto")

admin.site.register(Quarto)
admin.site.register(Cliente)
admin.site.register(Consumo)