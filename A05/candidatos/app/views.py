from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Candidato

def index(request):

    context = {
        'candidatos': Candidato.objects.order_by('-codigo').all()
    }

    return render(request, 'index.html', context)


def create(request):
    
    context = {
        'is_edit': False,
        'candidato': {
            'codigo': '',
            'nome': '',
            'sexo': '',
            'data_nasc': '',
            'cargo_pretendido': '',
            'texto_curriculo': '',
        }
    }
    
    return render(request, 'create-edit.html', context)


def insert(request):
    
    candidato = {
        'nome': request.POST.get('nome', ''),
        'sexo': request.POST.get('sexo', ''),
        'data_nasc': request.POST.get('data_nasc', ''),
        'cargo_pretendido': request.POST.get('cargo_pretendido', ''),
        'texto_curriculo': request.POST.get('texto_curriculo', ''),
    }
    
    Candidato.objects.create(**candidato)
    
    messages.add_message(request, messages.SUCCESS, 'Candidato criado com sucesso!')
    return redirect('index')


def edit(request, codigo):
    
    try:
        candidato = Candidato.objects.get(codigo=codigo)
        
        context = {
            'is_edit': True,
            'candidato': candidato
        }
        
        return render(request, 'create-edit.html', context)
    
    except Candidato.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Candidato inválido!')
        return redirect('index')


def update(request):
    
    try:
        candidato = Candidato.objects.get(codigo=request.POST.get('codigo', 0))
        
        candidato.nome = request.POST.get('nome', '')
        candidato.sexo = request.POST.get('sexo', '')
        candidato.data_nasc = request.POST.get('data_nasc', '')
        candidato.cargo_pretendido = request.POST.get('cargo_pretendido', '')
        candidato.texto_curriculo = request.POST.get('texto_curriculo', '')
        
        candidato.save()
    
        messages.add_message(request, messages.SUCCESS, 'Candidato atualizado com sucesso!')
        return redirect('index')
        
    except Candidato.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Candidato inválido!')
        return redirect('edit')
    

def delete(request, codigo):
    try:
        candidato = Candidato.objects.get(codigo=codigo)
        
        candidato.delete()
        
        messages.add_message(request, messages.SUCCESS, 'Candidato deletado com sucesso!')
        return redirect('index')
    
    except Candidato.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Candidato inválido!')
        return redirect('index')