from django.urls import path
from . import views

urlpatterns = [
    path('consulta/', views.consulta_cpf, name="consulta_cpf")

]