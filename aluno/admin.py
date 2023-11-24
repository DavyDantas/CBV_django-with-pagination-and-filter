from django.contrib import admin

from hospedagem.models import Cliente, Hospedagem, Quarto
from .models import Aluno,Cidade,Curso

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display=('nome_aluno','endereco','email')




