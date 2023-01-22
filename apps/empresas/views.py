from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self,  form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('Ok')


class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']


'''
============ Anotações ==============

Ao criar uma empresa nova, preciso que o funcionário que esteja criando ja se vincule a ela na sequência
Então depois de validar o forms, salvo os dados, pego o funcionario através do request do usuário, vinculo a empresa nele e salvo
'''