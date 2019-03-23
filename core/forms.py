from django.forms  import ModelForm, TextInput, Select, DateInput, EmailInput
from .models import Client, Automovel

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  #['name','age','sexo','rg','cpf','email','data_nascimento']
        widgets = {
            'name': TextInput(attrs={
                "placeholder":"Nome",
                "class":"form-control"
             }),
            'age':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Idade'
            }),
            'sexo': Select(attrs={
                'class':'form-control',
                'placeholder':"Sexo"
            }),
            'rg': TextInput(attrs={
                'class':'form-control',
                'rg-mask':''
            }),
            'cpf': TextInput(attrs={
                'class':'form-control',
                'cpf-mask':''
            }),
            'email': EmailInput(attrs={
                'class':'form-control',
            }),
            'data_nascimento': DateInput(attrs={
                'class':'form-control',
                'datemask':''
            })
        }

class AutomovelForm(ModelForm):
    class Meta:
        model = Automovel
        fields = ['marca','modelo','ano','cor'] #[marca, modelo, ano, cor]

