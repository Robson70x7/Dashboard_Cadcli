from ..models import Client
from django.utils import timezone
from django.shortcuts import get_object_or_404

class ServiceClient():
    def __init__(self):
        self.name = ''
        self.age = ''
        self.sexo = ''
        self.rg = ''
        self.cpf = ''
        self.email = ''
        self.data_nascimento = ''


    def verify_exist_email(self, email):
        lista = Client.objects.filter(email__exact = email)
        if lista:
            return True
        else:
            return False


    def get_all(self):
        """
        call -> c = Client.find_all()
        return -> Retorna todos clientes.
        """
        return Client.objects.all()

    
    def find(self, id):
        return get_object_or_404(Client, id=id)


    def create_auto(self, id, kwargs):
        client = self.find(id)
        auto = client.automovel_set.create(
            marca=kwargs['marca'], modelo=kwargs['modelo'],
            cor=kwargs['cor'], ano=kwargs['ano']
        )
        if auto:
            return True
        else:
            False


    def create(self):
        """
        fields -> (client)
        return -> object: Client
        """
        new_client = Client(
            name = self.name,
            age = self.age,
            sexo = self.sexo,
            rg = self.rg,
            cpf =self.cpf,
            email = self.email,
            data_nascimento = self.data_nascimento
        )
        new_client.save()
        return new_client


    def filter(**kwarg):
        return get_object_or_404(Client, kwarg)


    @property
    def latest(self):
        return Client.objects.latest('id')


    def delete(self, id):
        client = self.find(id)
        if client:
            client.delete()
            return True
        
        return False


    def update(self, id):
        client = self.find(id=id)
        
        return True

        