from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView,
from commondb.models.restaurant import Restaurant

class AdmiShopListView(ListView):
    model = Restaurant
    template_name = 'admi/shop_list.html'
    paginate_by = 10

class AdmiShopCreateView(CreateView):
    model = Restaurant
    template_name = 'admi/add_shop.html'
    fields = '__all__'
    success_url = reverse_lazy('admi:shop_list')
    
class AdmiShopUpdateView(UpdateView):
    model = Restaurant
    template_name = 'admi/edit_shop.html'
    fields = '__all__'
    