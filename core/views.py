from django.shortcuts import render, redirect
from .services.cliente import ServiceClient
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

def index(request):
    cli = ServiceClient()
    clients = cli.get_all()
    return render(request, 'core/index.html', {'clients':clients})

def create(request):
    return render(request, 'core/create.html')

def edit(request, client_id):
    return HttpResponse(f"Editar o cliente {client_id}")

def delete(request, client_id):
    return HttpResponse(f"Excluir o cliente {client_id}")

def detail (request, client_id):
    client = ServiceClient.find(id=client_id)
    return render(request, 'core/detail.html', {'client':client})

def saveclient(request):
    client = ServiceClient()
    client.name = request.POST['name']
    client.age = request.POST['age']
    client.sexo = request.POST['sexo']
    client.rg = request.POST['rg']
    client.cpf = request.POST['cpf']
    client.email = request.POST['email']

    data = str(request.POST['data_nascimento']).split('/')
    formato_datetime = [data[2], data[1], data[0]]
    newdata = '-'.join(formato_datetime)

    client.data_nascimento = newdata
    
    new_client = client.create();

    return redirect('core:create', {'client': new_client} )

