from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView,UpdateView,CreateView,DeleteView,ListView
from django.urls import reverse_lazy
from .models import *
from .forms import *

class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_hospedagens'] = Hospedagem.objects.count()
        return context

class HospedagemCriar(CreateView):
    template_name = 'form.html'
    form_class = hospedagemForm
    success_url = reverse_lazy('hospedagem_listar')

class HospedagemEditar(UpdateView):
    model = Hospedagem
    form_class = hospedagemForm
    template_name = 'form.html'
    pk_url_kwarg = 'pk'
    
    def get_success_url(self):
        return reverse_lazy('hospedagem_listar')

class HospedagemDeletar(DeleteView):
    model = Hospedagem
    success_url = reverse_lazy('hospedagem_listar')
    pk_url_kwarg = 'pk'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class HospedagemListar(ListView):
    model = Hospedagem
    template_name = 'hospedagens.html'
    context_object_name = 'hospedagens'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = HospedagemFilterForm(self.request.GET or None) 
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = HospedagemFilterForm(self.request.GET or None)
        if self.form.is_valid():
            if self.form.cleaned_data.get('cliente'):
                queryset = queryset.filter(cliente=self.form.cleaned_data['cliente'])
            if self.form.cleaned_data.get('quarto'):
                queryset = queryset.filter(quarto=self.form.cleaned_data['quarto'])
        return queryset

class HospedagemDetalhes(TemplateView):
    template_name = 'detalhes.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        context['hospedagem'] = get_object_or_404(Hospedagem, pk=pk)
        return context