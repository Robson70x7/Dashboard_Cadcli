from django.shortcuts import render
from django.http import HttpResponse
from .models import Client

def index(request):
    client = Client.objects.all()
    return render(request, 'core/index.html', {'client':client})

def create(request):
    return HttpResponse('Criar um cliente novo')

def edit(request, client_id):
    return HttpResponse(f"Editar o cliente {client_id}")

def delete(request, client_id):
    return HttpResponse(f"Excluir o cliente {client_id}")