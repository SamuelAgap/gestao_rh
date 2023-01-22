from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset


class FuncionariosEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamento']


class FuncionariosDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionariosCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamento']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = funcionario.nome.split(" ")[0]
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionariosCreate, self).form_valid(form)


'''
=== Anotações ===
Quando a view é acessada pra ver a lista dos funcionários, o método get_queryset é chamado. Então, irei sobrepor ele com minhas especificações
'''

