from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('sair', views.LoginView.as_view(), name='logout'),
    path('cadastro', views.RegisterView.as_view(), name='register')
]
