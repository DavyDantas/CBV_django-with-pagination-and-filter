from django.urls import path
from .views import *

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('Criar-hospedagem', HospedagemCriar.as_view(), name="hospedagem_criar"),
    path('Listar-hospedagens', HospedagemListar.as_view(), name="hospedagem_listar"),
    path('Editar-hospedagem/<int:pk>', HospedagemEditar.as_view(), name='hospedagem_editar'),
    path('Deletar-hospedagem/<int:pk>', HospedagemDeletar.as_view(), name="hospedagem_deletar"),
    path('Detalhes-hospedagem/<int:pk>', HospedagemDetalhes.as_view(), name="hospedagem_detalhes")
]