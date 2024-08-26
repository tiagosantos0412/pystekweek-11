from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),  # Rota para a página de login
    path('cadastrar/', views.cadastrar, name='cadastrar'),  # Rota para a página de cadastro
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('', views.redirect_to_login),  # Redireciona a URL raiz para a página de login
]
