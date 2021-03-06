from django.db import models

SEXO_CHOICES = (
    ('Masculino','Masculino'), 
    ('Feminino','Feminino') 
)

class Client(models.Model):
    name = models.CharField('Nome', max_length=50,)
    age = models.IntegerField( verbose_name='Idade')
    sexo = models.CharField('Sexo', max_length=10, choices= SEXO_CHOICES, default='')
    rg = models.CharField('RG', max_length=20)
    cpf = models.CharField('CPF', max_length=20)
    email = models.EmailField('E-mail', unique=True)
    data_nascimento = models.DateField('Data Nascimento')

    def __str__(self):
        return self.name

    class Meta:
        ordering = 'name',
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Automovel(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=50)
    ano = models.CharField('Ano', max_length=10)
    cor = models.CharField(max_length=15)

    def __str__(self):
        return f'Modelo: {self.modelo}, Marca: {self.marca}'
        

class Endereco(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=9)
    cidade= models.CharField(max_length=30)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    uf = models.CharField(max_length=2)

    def __str__(self):
        
        return f"Rua: {self.logradouro} - {self.numero} - {self.bairro} - {self.cidade}, {self.estado} - {self.uf}"

class Telefone(models.Model):
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    celular_1 = models.CharField(max_length=20)
    celular_2 = models.CharField(max_length=20)
    fixo = models.CharField(max_length=20)
    
    def __str__(self):
        return self.celular_1