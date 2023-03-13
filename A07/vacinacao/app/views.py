from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Usuario

def index(request):

    context = {
        'is_search': False,
        'usuarios': Usuario.objects.order_by('-id').all()
    }

    return render(request, 'index.html', context)

def search(request):
    
    id = request.GET.get('id', None)
    
    if id is not None:
            
        context = {
            'is_search': True,
            'search_id': id,
            'usuarios': Usuario.objects.filter(id=id).all()
        }

        return render(request, 'index.html', context)
    
    else:
        return redirect('index')


def create(request):
    
    context = {
        'is_edit': False,
        'usuario': {
            'id': '',
            'nome': '',
            'dt_nasc': '',
            'sexo': '',
            'lougradouro': '',
            'numero': '',
            'setor': '',
            'cidade': '',
            'uf': '',
        }
    }
    
    return render(request, 'create-edit.html', context)


def insert(request):
    
    usuario = {
        'nome': request.POST.get('nome', ''),
        'dt_nasc': request.POST.get('dt_nasc', ''),
        'sexo': request.POST.get('sexo', ''),
        'lougradouro': request.POST.get('lougradouro', ''),
        'numero': request.POST.get('numero'),
        'setor': request.POST.get('setor', ''),
        'cidade': request.POST.get('cidade', ''),
        'uf': request.POST.get('uf', ''),
    }
    
    Usuario.objects.create(**usuario)
    
    messages.add_message(request, messages.SUCCESS, 'Usuário criado com sucesso!')
    return redirect('index')


def edit(request, id):
    
    try:
        usuario = Usuario.objects.get(id=id)
        
        context = {
            'is_edit': True,
            'usuario': usuario
        }
        
        return render(request, 'create-edit.html', context)
    
    except Usuario.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Usuário inválido!')
        return redirect('index')


def update(request):
    
    try:
        usuario = Usuario.objects.get(id=request.POST.get('id', 0))
        
        usuario.nome = request.POST.get('nome', '')
        usuario.dt_nasc = request.POST.get('dt_nasc', '')
        usuario.sexo = request.POST.get('sexo', '')
        usuario.lougradouro = request.POST.get('lougradouro', '')
        usuario.numero = request.POST.get('numero')
        usuario.setor = request.POST.get('setor', '')
        usuario.cidade = request.POST.get('cidade', '')
        usuario.uf = request.POST.get('uf', '')
        
        usuario.save()
    
        messages.add_message(request, messages.SUCCESS, 'Usuário atualizado com sucesso!')
        return redirect('index')
        
    except Usuario.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Usuário inválido!')
        return redirect('edit')
    

def delete(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        
        usuario.delete()
        
        messages.add_message(request, messages.SUCCESS, 'Usuário deletado com sucesso!')
        return redirect('index')
    
    except Usuario.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Usuário inválido!')
        return redirect('index')