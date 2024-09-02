from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    #path('api/dados-cliente/', views.home, name='api_dados_cliente'),  # Nova URL para a API
    path('', views.redirect_to_login),
]
