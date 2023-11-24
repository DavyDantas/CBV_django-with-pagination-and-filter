from django.views.generic import TemplateView,UpdateView,CreateView,DeleteView,ListView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render,get_object_or_404,redirect
from .models import Aluno,Curso,Cidade
from .forms import AlunoForm,AlunoFilterForm


class AlunoCriar(CreateView):
    template_name = 'aluno/form.html'
    form_class = AlunoForm
    success_url = reverse_lazy('aluno_listar')

class AlunoEditar(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/form.html'
    pk_url_kwarg = 'id' # Nome da variável na URL
    
    def get_success_url(self):
        return reverse_lazy('aluno_listar')

class AlunoRemover(DeleteView):
    model = Aluno
    success_url = reverse_lazy('aluno_listar')
    pk_url_kwarg = 'id'

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
    
class AlunoListar(ListView):
    model = Aluno
    template_name = 'aluno/alunos.html'
    context_object_name = 'alunos'  # Nome da variável a ser usada no template
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AlunoFilterForm(self.request.GET or None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = AlunoFilterForm(self.request.GET or None)
        if self.form.is_valid():
            if self.form.cleaned_data.get('nome'):
                queryset = queryset.filter(nome_aluno__icontains=self.form.cleaned_data['nome'])
            if self.form.cleaned_data.get('cidade'):
                queryset = queryset.filter(cidade=self.form.cleaned_data['cidade'])
            if self.form.cleaned_data.get('curso'):
                queryset = queryset.filter(curso=self.form.cleaned_data['curso'])
        return queryset

class IndexView(TemplateView):
    template_name = "aluno/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_alunos'] = Aluno.objects.count()
        context['total_cidades'] = Cidade.objects.count()
        context['total_cursos'] = Curso.objects.count()
        return context


