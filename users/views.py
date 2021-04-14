from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.views import generic
from users import forms
from core.models import Seller
from django.db import transaction


class LogoutView(auth_views.LogoutView):
    template_name = 'users/login.html'


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    form_class = forms.LoginForm


class RegisterView(generic.FormView):
    form_class = forms.RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    @transaction.atomic
    def form_valid(self, form):
        user = form.save()
        Seller.objects.create(user=user, city=form.cleaned_data['city'])
        return HttpResponseRedirect(self.get_success_url())
