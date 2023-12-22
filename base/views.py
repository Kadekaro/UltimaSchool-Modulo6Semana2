from django.shortcuts import render
from base.forms import inscreverContato, reservarBanho


def inicio(request):
    return render(request, "inicio.html")


def contato(request):
    contexto = {'sucesso': False}
    if request.method == 'POST':
        form = inscreverContato(request.POST)
        if form.is_valid():
            nome = request.POST['nome']
            email = request.POST['email']
            telefone = request.POST['telefone']
            contexto['sucesso'] = True
    else:
        form = inscreverContato()
    contexto['form'] = form
    return render(request, "contato.html", contexto)


def reservaDeBanho(request):
    contexto = {'sucesso': False}
    if request.method == "POST":
        form = reservarBanho(request.POST)
        if form.is_valid():
            nome_do_animal = request.POST['nome_pet']
            telefone = request.POST['telefone']
            data = request.POST['data']
            observacao = request.POST['observacao']
            contexto['sucesso'] = True
    else:
        form = reservarBanho()
    contexto['form'] = form
    return render(request, "reservar_banho.html", contexto)
