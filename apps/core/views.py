from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario


@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)


'''
======== Anotações ===========

Importei o login_required pra usar como decorator
Quando eu digo que o login é requerido pra acessar a home, ninguem consegue ir pra home direto antes de logar
'''