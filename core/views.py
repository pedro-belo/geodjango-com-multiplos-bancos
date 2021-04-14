from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from core import forms, models

# Create your views here.


class MapView(generic.TemplateView):
    template_name = 'core/map.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update({'form': forms.FormSelectProduct})
        return kwargs


class DashboardView(LoginRequiredMixin, generic.ListView):
    template_name = 'core/dashboard.html'
    context_object_name = 'items'

    def get_queryset(self):
        return models.Marketplace.objects.filter(seller__user=self.request.user)


class MarketplaceCreateView(LoginRequiredMixin, generic.FormView):
    form_class = forms.MarketplaceForm
    template_name = 'core/marketplace/create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        try:
            obj = form.save(commit=False)
            obj.seller = self.request.user.seller
            obj.save()
        except Exception:
            # IntegrityError...
            pass

        return redirect('core:dashboard')


class MarketplaceDeleteView(LoginRequiredMixin, generic.DeleteView):

    success_url = reverse_lazy('core:dashboard')

    def get_queryset(self):
        return models.Marketplace.objects.filter(seller__user=self.request.user)
