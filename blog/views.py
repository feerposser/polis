from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import ModelContato


def index(request):
    return render(request, 'blog/index.html')


def send_message(request):
    # todo alterar para forms
    try:
        contact = ModelContato()

        contact.nome = request.POST['nome']
        contact.email = request.POST['email']
        contact.assunto = request.POST['assunto']
        contact.mensagem = request.POST['mensagem']

        contact.save()

        return HttpResponseRedirect(reverse('mensagem_enviada', args=['sucesso']))
    except Exception as e:
        return HttpResponseRedirect(reverse('mensagem_enviada', args=['falha']))