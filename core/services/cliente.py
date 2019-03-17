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

    def find(self,id):
        return get_object_or_404(Client, id=id)

    
    def get_all(self):
        """
        call -> c = Client.find_all()
        return -> Retorna todos clientes.
        """
        return Client.objects.all()


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


    def delete(self):
        pass

    def edit(self):
        pass