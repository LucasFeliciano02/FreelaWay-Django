from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


# Para cada (path), tem uma função em views 

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),  # meudominio.com.br/auth/cadastro
    path('logar/', views.logar, name='logar'),  # meudominio.com.br/auth/logar
    path('sair/', views.sair, name="sair"),  # meudominio.com.br/auth/sair
    
    # Esses paths, sao chamados nos html de login desse app, por isso nao tem funções em views
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm_view.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete")
]


# http://127.0.0.1:8000/auth/cadastro/

# http://127.0.0.1:8000/auth/logar/

# meudominio.com.br/auth/cadastro

# cadastro, logar, sair é a função que esta em views
