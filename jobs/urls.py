from django.urls import path
from . import views


urlpatterns = [
    path('encontrar_jobs/', views.encontrar_jobs, name='encontrar_jobs'),
    path('aceitar_job/<int:id>/', views.aceitar_job, name='aceitar_job'),
    path('perfil/', views.perfil, name='perfil'),
    path('enviar_projeto/', views.enviar_projeto, name='enviar_projeto')
]

# Através do 'id' que o usuario vai aceitar, sabemos qual é o job aceitado, ex: req para: dominio.com/aceitar job/1, o usuario aceitou o 'job 1' e vamos conseguir receber isso através da view

# A função em views tem que ter o mesmo nome do path da urls.py
