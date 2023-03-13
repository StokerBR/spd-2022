from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Usuario, Alergia, Vacina, Agenda
from .enums import Periodicidade, Situacao
from datetime import datetime
from dateutil.relativedelta import relativedelta

def home(request):
    return render(request, 'home.html')

# Usuário --------------------------------------------------

def user_index(request):

    context = {
        'is_search': False,
        'usuarios': Usuario.objects.order_by('-id').all()
    }

    return render(request, 'user/index.html', context)


def user_create(request):

    context = {
        'is_edit': False,
        'usuario': {
            'id': '',
            'nome': '',
            'data_nascimento': '',
            'sexo': '',
            'lougradouro': '',
            'numero': '',
            'setor': '',
            'cidade': '',
            'uf': '',
        }
    }

    return render(request, 'user/create-edit.html', context)


def user_insert(request):

    usuario = {
        'nome': request.POST.get('nome', ''),
        'data_nascimento': request.POST.get('data_nascimento', None),
        'sexo': request.POST.get('sexo', ''),
        'lougradouro': request.POST.get('lougradouro', ''),
        'numero': request.POST.get('numero'),
        'setor': request.POST.get('setor', ''),
        'cidade': request.POST.get('cidade', ''),
        'uf': request.POST.get('uf', ''),
    }

    Usuario.objects.create(**usuario)

    messages.add_message(request, messages.SUCCESS, 'Usuário criado com sucesso!')
    return redirect('user_index')


def user_edit(request, id):

    try:
        usuario = Usuario.objects.get(id=id)

        context = {
            'is_edit': True,
            'usuario': usuario
        }

        return render(request, 'user/create-edit.html', context)

    except Usuario.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Usuário inválido!')
        return redirect('user_index')


def user_update(request):

    try:
        usuario = Usuario.objects.get(id=request.POST.get('id', 0))

        usuario.nome = request.POST.get('nome', '')
        usuario.data_nascimento = request.POST.get('data_nascimento', '')
        usuario.sexo = request.POST.get('sexo', '')
        usuario.lougradouro = request.POST.get('lougradouro', '')
        usuario.numero = request.POST.get('numero')
        usuario.setor = request.POST.get('setor', '')
        usuario.cidade = request.POST.get('cidade', '')
        usuario.uf = request.POST.get('uf', '')

        usuario.save()

        messages.add_message(request, messages.SUCCESS, 'Usuário atualizado com sucesso!')
        return redirect('user_index')

    except Usuario.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Usuário inválido!')
        return redirect('user_edit')


def user_delete(request, id):
    try:
        usuario = Usuario.objects.get(id=id)

        usuario.delete()

        messages.add_message(request, messages.SUCCESS, 'Usuário deletado com sucesso!')
        return redirect('user_index')

    except Usuario.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Usuário inválido!')
        return redirect('user_index')

# Alergia --------------------------------------------------

def allergy_index(request, usuario_id):

    usuario = Usuario.objects.get(id=usuario_id)

    context = {
        'alergias': Alergia.objects.filter(usuario=usuario).order_by('-id').all(),
        'usuario': usuario
    }

    return render(request, 'allergy/index.html', context)


def allergy_create(request, usuario_id):

    context = {
        'usuario_id': usuario_id
    }

    return render(request, 'allergy/create.html', context)


def allergy_insert(request, usuario_id):

    usuario = Usuario.objects.get(id=usuario_id)

    alergia = {
        'nome': request.POST.get('nome', ''),
        'usuario': usuario
    }

    Alergia.objects.create(**alergia)

    messages.add_message(request, messages.SUCCESS, 'Alergia cadastrada com sucesso!')
    return redirect('allergy_index', usuario_id=usuario_id)


def allergy_delete(request, usuario_id, id):
    try:
        allergy = Alergia.objects.get(id=id)

        allergy.delete()

        messages.add_message(request, messages.SUCCESS, 'Agenda deletada com sucesso!')
        return redirect('allergy_index', usuario_id=usuario_id)

    except Alergia.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Agenda inválida!')
        return redirect('allergy_index', usuario_id=usuario_id)

# Vacina --------------------------------------------------

def vaccine_index(request):

    context = {
        'vacinas': Vacina.objects.order_by('-id').all(),
        'periodicidades': {i.value: i.name for i in Periodicidade}
    }

    return render(request, 'vaccine/index.html', context)

def vaccine_create(request):

    context = {
        'is_edit': False,
        'vacina': {
            'id': '',
            'titulo': '',
            'descricao': '',
            'doses': '',
            'periodicidade': '',
            'intervalo': '',
        }
    }

    return render(request, 'vaccine/create-edit.html', context)

def vaccine_insert(request):

    vacina = {
        'titulo': request.POST.get('titulo', ''),
        'descricao': request.POST.get('descricao', ''),
        'doses': request.POST.get('doses'),
        'periodicidade': request.POST.get('periodicidade'),
        'intervalo': request.POST.get('intervalo'),
    }

    Vacina.objects.create(**vacina)

    messages.add_message(request, messages.SUCCESS, 'Vacina cadastrada com sucesso!')
    return redirect('vaccine_index')

def vaccine_edit(request, id):

    try:
        vacina = Vacina.objects.get(id=id)

        context = {
            'is_edit': True,
            'vacina': vacina
        }

        return render(request, 'vaccine/create-edit.html', context)

    except Vacina.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Vacina inválida!')
        return redirect('vaccine_index')

def vaccine_update(request):

    try:
        vacina = Vacina.objects.get(id=request.POST.get('id', 0))

        vacina.titulo = request.POST.get('titulo', '')
        vacina.descricao = request.POST.get('descricao', '')
        vacina.doses = request.POST.get('doses')
        vacina.periodicidade = request.POST.get('periodicidade')
        vacina.intervalo = request.POST.get('intervalo')

        vacina.save()

        messages.add_message(request, messages.SUCCESS, 'Vacina atualizada com sucesso!')
        return redirect('vaccine_index')

    except Vacina.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Vacina inválida!')
        return redirect('vaccine_edit')

def vaccine_delete(request, id):
    try:
        vacina = Vacina.objects.get(id=id)

        vacina.delete()

        messages.add_message(request, messages.SUCCESS, 'Vacina deletada com sucesso!')
        return redirect('vaccine_index')

    except Usuario.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Vacina inválida!')
        return redirect('vaccine_index')

# Agenda --------------------------------------------------

def schedule_index(request):

    situacao = request.GET.get('situacao', None)

    agendas = []

    if situacao:
        agendas = Agenda.objects.order_by('-id').filter(situacao=situacao).all()
    else:
        agendas = Agenda.objects.order_by('-id').all()

    context = {
        'situacao': situacao,
        'situacoes': {i.name for i in Situacao},
        'agendas': agendas,
    }

    return render(request, 'schedule/index.html', context)


def schedule_create(request):

    context = {
        'usuarios': Usuario.objects.order_by('nome').all(),
        'vacinas': Vacina.objects.order_by('titulo').all(),
    }

    return render(request, 'schedule/create.html', context)


def schedule_insert(request):

    schedule = {
        'usuario': Usuario.objects.get(id=request.POST.get('usuario_id', 0)),
        'vacina': Vacina.objects.get(id=request.POST.get('vacina_id', 0)),
        'data': request.POST.get('data', ''),
        'hora': request.POST.get('hora', ''),
        'observacoes': request.POST.get('observacoes', ''),
        'situacao': Situacao.AGENDADO.name
    }

    date = datetime.strptime(schedule['data'], '%Y-%m-%d')

    vaccine = schedule['vacina']
    frequency = vaccine.periodicidade
    interval = vaccine.intervalo
    doses = vaccine.doses

    dateAddition = None

    if frequency == Periodicidade.DIA.value:
        dateAddition = relativedelta(days=interval)
    elif frequency == Periodicidade.SEMANA.value:
        dateAddition = relativedelta(weeks=interval)
    elif frequency == Periodicidade.MES.value:
        dateAddition = relativedelta(months=interval)
    elif frequency == Periodicidade.ANO.value:
        dateAddition = relativedelta(years=interval)


    for i in range(doses):
        schedule['data'] = date.strftime("%Y-%m-%d")
        Agenda.objects.create(**schedule)
        date += dateAddition

    messages.add_message(request, messages.SUCCESS, 'Agenda criada com sucesso!')
    return redirect('schedule_index')


def schedule_perform(request, id):

    schedule = Agenda.objects.get(id=id)

    schedule.situacao = Situacao.REALIZADO.name
    schedule.data_situacao = datetime.now().strftime("%Y-%m-%d")

    schedule.save()

    messages.add_message(request, messages.SUCCESS, 'Agenda realizada com sucesso!')
    return redirect('schedule_index')


def schedule_cancel(request, id):

    schedule = Agenda.objects.get(id=id)

    schedule.situacao = Situacao.CANCELADO.name
    schedule.data_situacao = datetime.now().strftime("%Y-%m-%d")

    schedule.save()

    messages.add_message(request, messages.SUCCESS, 'Agenda cancelada com sucesso!')
    return redirect('schedule_index')


def schedule_delete(request, id):
    try:
        schedule = Agenda.objects.get(id=id)

        schedule.delete()

        messages.add_message(request, messages.SUCCESS, 'Agenda deletada com sucesso!')
        return redirect('schedule_index')

    except Agenda.DoesNotExist:
        messages.add_message(request, messages.ERROR, 'Agenda inválida!')
        return redirect('schedule_index')
