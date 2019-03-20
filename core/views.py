from django.shortcuts import render, redirect
from .services.cliente import ServiceClient
from django.views.decorators import http
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.urls import reverse
from .forms import ClientForm

@http.require_GET
def index(request):
    cli = ServiceClient()
    clients = cli.get_all()
    context_view = {'clients':clients}

    if 'messages' in request.session:
        messages = request.session.pop('messages')
        context_view.update(messages)

    return render(request, 'core/index.html', context= context_view)


def create(request):
    form = ClientForm()

    context_view = {'form':form}

    if request.method == 'POST':
        form_preenchido = ClientForm(data=request.POST)
        if form_preenchido.is_valid():
            form_preenchido.save()
            request.session['messages'] = {'success_message':'Cliente cadastrado com sucesso'}
        else:
            request.session['messages'] = {'error_message':'O formulario enviado esta com inválido, preencha novamente e envie'}
            return redirect('create')
    
    if 'messages' in request.session:
        message = request.session.pop('messages')
        context_view.update(message)
    return render(request, 'core/create.html', context= context_view)


def edit(request, client_id):
    client = ServiceClient().find(client_id)
    form = ClientForm(request.POST or None, instance=client)
    context_view = {}

    if request.method == 'POST':
        if form.is_valid(): 
            form.save()
            context_view['success_message'] = 'Atualização feita com sucesso!'
        else:
            return redirect('edit', client_id)

    context_view.update({'form':form, 'client_id':client.id})
    return render(request, 'core/edit.html', context= context_view) 
    context_view.clear()


def delete(request, client_id):
    if 'messages' in request.session:
        request.session.flush()

    if ServiceClient().delete(client_id):
        request.session['messages'] = {'success_message':'Cliente excluido com sucesso'}
        return redirect('/')
    else:
        request.session['messages'] = {'error_message':'Falha ao excluido cliente, atualiza a pagina e tente novamente'}
        return redirect('/')


@http.require_GET
def detail (request, client_id):
    client = ServiceClient()
    result = client.find(id= client_id)

    return render(request, 'core/detail.html', {'client':result})