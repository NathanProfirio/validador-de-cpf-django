from django.urls import path
from . import views

urlpatterns = [
    path('', views.consulta_cpf, name="consulta_cpf")

]