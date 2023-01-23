from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100, help_text='Descrição do documento')
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.descricao


    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.pertence.id])
    '''
    ============ Anotações ========
    
    Linha 7 - Um proprietário/funcionário pode ter mais de 1 documento, por isso utiliza chave
    '''
