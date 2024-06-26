from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from commondb.models.reguration import Reguration
from django.shortcuts import get_object_or_404
from ..views.login_permission_view import AdmiRequiredView


class RegTemplateView(AdmiRequiredView, TemplateView):
    model = Reguration
    template_name = 'admi/reguration.html'
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(Reguration, pk=2)
        return context
        
class RegUpdateView(AdmiRequiredView, UpdateView):
    model = Reguration
    template_name = 'admi/edit_reguration.html'
    fields = '__all__'
    success_url = reverse_lazy('admi:reguration')
    