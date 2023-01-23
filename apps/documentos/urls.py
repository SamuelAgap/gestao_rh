from django.urls import path
from .views import DocumentosCreate

urlpatterns = [
    path('novo/<int:funcionario_id>/', DocumentosCreate.as_view(), name='create_documentos'),

]
