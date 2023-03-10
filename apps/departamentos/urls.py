from django.urls import path
from .views import DepartamentosList, DepartamentosCreate, DepartamentosUpdate, DepartamentosDelete

urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo', DepartamentosCreate.as_view(), name='create_departamentos'),
    path('editar/<int:pk>/', DepartamentosUpdate.as_view(), name='update_departamentos'),
    path('delete/<int:pk>/', DepartamentosDelete.as_view(), name='delete_departamentos'),
]