from django.shortcuts import render, redirect
from .services.cliente import ServiceClient
from django.views.decorators import http
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

@http.require_GET
def index(request):
    cli = ServiceClient()
    clients = cli.get_all()
    return render(request, 'core/index.html', {'clients':clients})
@http.require_GET
def create(request):
    return render(request, 'core/create.html')

@http.require_GET
def edit(request, client_id):
    client = ServiceClient().find(client_id)
    return render(request, 'core/edit.html', {'client': client})


@http.require_POST
def edit_post(request, client_id):
    name = request.POST['name']
    age = request.POST['age']
    sexo = request.POST['sexo']
    rg = request.POST['rg']
    cpf = request.POST['cpf']
    email = request.POST['email']
    cli = ServiceClient().update(name=name, age=age, sexo=sexo, rg=rg, cpf=cpf, email=email)


@http.require_GET
def delete(request, client_id):
    return HttpResponse(f"Excluir o cliente {client_id}")


@http.require_GET
def detail (request, client_id):
    client = ServiceClient.find(id=client_id)
    return render(request, 'core/detail.html', {'client':client})

@http.require_POST
def saveclient(request):
    client = ServiceClient()
    client.name = request.POST['name']
    client.age = request.POST['age']
    client.sexo = request.POST['sexo']
    client.rg = request.POST['rg']
    client.cpf = request.POST['cpf']
    client.email = request.POST['email']

    #Trabalhando o formato de data adequado.
    data = str(request.POST['data_nascimento']).split('/')
    formato_datetime = [data[2], data[1], data[0]]
    newdata = '-'.join(formato_datetime)
    client.data_nascimento = newdata

    #Salvando na base de dados
    new_client = client.create();

    return render(request, 'core/create.html', {'client': new_client, 'successmessage': True} )

