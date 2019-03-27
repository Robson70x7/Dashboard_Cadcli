from django.shortcuts import render, redirect
from  .services.cliente import ServiceClient
from django.views.decorators import http
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from datetime import datetime
from django.urls import reverse
from .forms import ClientForm, AutomovelForm

service_client = ServiceClient()

service_client = ServiceClient()

@http.require_GET
def index(request):
<<<<<<< HEAD
    cli = service_client
    clients = cli.get_all()
=======
    clients = service_client.get_all()
>>>>>>> e7c44c25d6af16bcdc69b961a15878a46ff1e9b4
    context_view = {'clients':clients}
    
    if 'messages' in request.session:
        messages = request.session.pop('messages')
        context_view.update(messages)

    return render(request, 'core/index.html', context= context_view)


def create(request):
    """Criar novo usuario """
    form = ClientForm()
    #Implementar o form de Automovel
    form_auto = AutomovelForm()
    context_view = {'form':form, 'form_auto':form_auto}
    
    if request.method == 'POST':
        dispose_session(request)
        dados = request.POST
        fields_auto = ['client_id','marca','modelo','ano','cor']
        dados_client = {key:value for key,value in dados.items() if key not in fields_auto}
        dados_auto = {key:value for key,value in dados.items() if key in fields_auto}

        form_preenchido = ClientForm(dados_client or None)

        if form_preenchido.is_valid():
            #Verificações
            if service_client.verify_exist_email(dados['email']):
                request.session['messages'] = {'error_message':'Este email ja existe em nossa base de dados, corrija-o e tente novamente'}
                context_view['form'] = form_preenchido
                context_view.update(request.session.pop('messages'))
                return render(request, 'core/create.html', context= context_view)

            new_client = form_preenchido.save()
        else:
            request.session['messages'] = {'error_message':'O formulario enviado esta inválido, preencha novamente e envie'}
            return redirect('core:create')

        #Formulario de Automovel
<<<<<<< HEAD
=======
        #client = service_client.latest  # recupera ultimo dado cadastrado
>>>>>>> e7c44c25d6af16bcdc69b961a15878a46ff1e9b4
        cad_auto = service_client.create_auto(new_client.id, dados_auto)

        if not cad_auto:
            request.session['messages'] = {'error_message':'Cliente cadastrado, porém, Automovel Não cadastrou'}
<<<<<<< HEAD
            redirect('core:create')
=======
>>>>>>> e7c44c25d6af16bcdc69b961a15878a46ff1e9b4
        else:
            request.session['messages'] = {'success_message':'Cliente, e automovel cadastrado com sucesso'}
        
    
    if 'messages' in request.session:
        message = request.session.pop('messages')
        context_view.update(message)

    return render(request, 'core/create.html', context= context_view)


def edit(request, client_id):
<<<<<<< HEAD
=======
    dispose_session(request)
>>>>>>> e7c44c25d6af16bcdc69b961a15878a46ff1e9b4
    client = service_client.find(client_id)
    form = ClientForm(request.POST or None, instance=client)
    context_view = {'form':form, 'client_id':client.id}
    
    if request.method == 'POST':
        if form.is_valid(): 
            form.save()
            request.session['messages'] = {'success_message':'Atualização feita com sucesso'}
        else:
            request.session['messages'] = {'error_message':'Erro ao Atualiziar cliente'}
            context_view.update(request.session.pop('messages'))
            return render(request, 'core/edit.html', context= context_view) 

    if 'messages' in request.session:
        context_view.update(request.session.pop('messages'))

    return render(request, 'core/edit.html', context= context_view) 


def delete(request, client_id):
    dispose_session(request)

    if service_client.delete(client_id):
        request.session['messages'] = {'success_message':'Cliente excluido com sucesso'}
        return redirect('/')
    else:
        request.session['messages'] = {'error_message':'Falha ao excluido cliente, atualiza a pagina e tente novamente'}
        return redirect('/')


def detail (request, client_id):
    client = service_client
    result = client.find(id= client_id)

    return render(request, 'core/detail.html', {'client':result})

def dispose_session(request):
    if 'messages' in request.session:
        request.session.flush()