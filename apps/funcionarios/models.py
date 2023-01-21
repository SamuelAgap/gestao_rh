from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do funcionário')
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


    '''
    ==================== Anotações ===================
    
    Linha 9 - Um usuário terá ligação com apenas um funcionário, e 1 funcionário com apenas 1 usuário. Além disso, pra deletar o usuário, ele precisa antes deletar o funcionário, poois ta protegido pelo PROTECT
    
    Linha 10 - Um funcionário pode ter vários/muitos/many departamentos e vice versa, um departamento pode ter muito funcionário. Ou seja, muitos pra muitos.
    
    Linha 11 - Um funcionário pode estar numa empresa, e quando alguem tentar deletar a empresa, primeiro terá de deletar o funcionário dela e só depois a empresa (protegido pelo PROTECT)
    '''