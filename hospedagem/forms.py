from django import forms
from .models import *
import datetime

class DateInput(forms.DateInput):
    super(forms.DateInput)
    input_type = 'date'

class hospedagemForm(forms.ModelForm):
    class Meta:
        model = Hospedagem
        fields = '__all__'
        widgets = {
            'data_entrada' : DateInput(attrs={'input_type':'date' ,'class': 'form-control '}),
            'data_saida' : DateInput(attrs={'class': 'form-control' }),
            'valor' : forms.NumberInput(attrs={'class': 'form-control' }),
            'cliente': forms.Select(attrs={'class': 'form-control' }),
            'quarto': forms.Select(attrs={'class': 'form-control' }),
        }

class HospedagemFilterForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=False)
    quarto = forms.ModelChoiceField(queryset=Quarto.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(HospedagemFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'