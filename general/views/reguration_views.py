from django.urls import reverse
from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from commondb.models.reguration import Reguration
from django.shortcuts import get_object_or_404


class RegTemplateView(TemplateView):
    model = Reguration
    template_name = 'general/reguration.html'
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['object'] = get_object_or_404(Reguration, pk=2)
        context['previous_page'] = self.request.META.get('HTTP_REFERER', reverse('top'))  # 前のページのURLを取得        
        return context