from django.shortcuts import render, redirect
from .models import Automovel
from  .services.cliente import ServiceClient
from django.views.decorators import http
from django.urls import reverse
from .forms import ClientForm, AutomovelForm

service_client = ServiceClient()

@http.require_GET
def index(request):
    clients = service_client.get_all()
    context_view = {'clients':clients}
    
    if 'messages' in request.session:
        messages = request.session.pop('messages')
        context_view.update(messages)

    return render(request, 'core/index.html', context=context_view)

def create(request):
    """Criar novo usuario """
    form = ClientForm()
    # Implementar o form de Automovel
    form_auto = AutomovelForm()
    context_view = {'form':form, 'form_auto':form_auto}
    
    if request.method == 'POST':

        dados = request.POST
        fields_auto = ['marca','modelo','ano','cor']
        dados_client = {key:value for key,value in dados.items() if key not in fields_auto}
        dados_auto = {key:value for key,value in dados.items() if key in fields_auto}

        form_preenchido = ClientForm(dados_client or None)

        if form_preenchido.is_valid():
            #Verifica se email já exist
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
        #client = service_client.latest  # recupera ultimo dado cadastrado
        cad_auto = service_client.create_auto(new_client.id, dados_auto)

        if not cad_auto:
            request.session['messages'] = {'error_message':'Cliente cadastrado, porém, Automovel Não cadastrou'}
        else:
            request.session['messages'] = {'success_message':'Cliente, e automovel cadastrado com sucesso'}
        
    if 'messages' in request.session:
        message = request.session.pop('messages')
        context_view.update(message)

    return render(request, 'core/create.html', context= context_view)

def edit(request, client_id):
    client = service_client.find(client_id)
    form = ClientForm(request.POST or None, instance=client)

    auto = client.automovel_set.first()
    form_auto = AutomovelForm(request.POST or None, instance=auto)

    context_view = {'form': form, 'form_auto':form_auto, 'client': client}

    if 'messages' in request.session:
        context_view.update(request.session.pop('messages'))

    return render(request, 'core/edit.html', context=context_view)
    
def edit_client(request, client_id):
    client = service_client.find(client_id)
    form = ClientForm(request.POST, instance=client)
    
    if form.is_valid(): 
        form.save()
        request.session['messages'] = {'success_message': 'Atualização feita com sucesso'}
    else:
        request.session['messages'] = {'error_message': 'Erro ao Atualiziar cliente'}

    return redirect('core:edit', client_id=client_id)

def edit_automovel(request, client_id):
    client = service_client.find(client_id)
    auto = Automovel.objects.get(client=client.id)
    form_auto = AutomovelForm(request.POST, instance=auto) 
    if form_auto.is_valid():
        form_auto.save()
        request.session['messages'] = {'success_message': 'Atualiziação feita com sucesso'}
    else:
        request.session['messages'] = {'error_message': 'Erro ao Atualiziar Automovel', 'errors_form': form_auto.errors}

    return redirect('core:edit', client_id=client_id)

def delete(request, client_id):
    if service_client.delete(client_id):
        request.session['messages'] = {'success_message': 'Cliente excluido com sucesso'}
        return redirect('/')
    else:
        request.session['messages'] = {'error_message': 'Falha ao excluido cliente, atualiza a pagina e tente novamente'}
        return redirect('/')

def detail(request, client_id):
    client = service_client.find(id=client_id)
    form = ClientForm(instance=client)
    return render(request, 'core/detail.html', {'form': form, 'client': client})

def imprimir(request, client_id):
    client = service_client.find(id=client_id)
    return render(request, 'core/print.html', {'client':client})    
