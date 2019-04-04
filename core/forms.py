from django import forms
from .models import Client, Automovel

class ClientForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control', 'placeholder':'Nome'})
        self.fields['age'].widget.attrs.update({'class':'form-control', 'placeholder':'Idade'})
        self.fields['sexo'].widget.attrs.update({'class':'form-control', 'placeholder':'Sexo'})
        self.fields['rg'].widget.attrs.update({'class':'form-control', 'placeholder':'Rg'})
        self.fields['cpf'].widget.attrs.update({'class':'form-control', 'placeholder':'CPF'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'E-mail'})
        self.fields['data_nascimento'].widget.attrs.update({'class':'form-control', 'datemask':''})

    
    class Meta:
        model = Client
        fields = '__all__'  #['name','age','sexo','rg','cpf','email','data_nascimento']


class AutomovelForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AutomovelForm, self).__init__(*args, **kwargs)
        self.fields['marca'].widget.attrs.update({'class':'form-control', 'placeholder':'Marca'})
        self.fields['modelo'].widget.attrs.update({'class':'form-control', 'placeholder':'Modelo'})
        self.fields['ano'].widget.attrs.update({'class':'form-control', 'placeholder':'Ano'})
        self.fields['cor'].widget.attrs.update({'class':'form-control', 'placeholder':'Cor'})


    class Meta:
        model = Automovel
        fields = '__all__'  #[client, marca, modelo, ano, cor]
       