from django.forms import ModelForm
from django import forms
from .models import Aluno,Curso,Cidade

class AlunoForm(ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'nome_aluno' : forms.TextInput(attrs={'class': 'form-control' }),
            'endereco' : forms.TextInput(attrs={'class': 'form-control' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'cidade': forms.Select(attrs={'class': 'form-control' }),
            'curso': forms.Select(attrs={'class': 'form-control' })
        }

class AlunoFilterForm(forms.Form):
    nome = forms.CharField(max_length=150, required=False)
    cidade = forms.ModelChoiceField(queryset=Cidade.objects.all(), required=False)
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=False)
    
    # adicionar a classe form-control para todos os campos
    def __init__(self, *args, **kwargs):
        super(AlunoFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
