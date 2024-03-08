from django.urls import path
from .views.company_views import CompanyUpdateView
from .views.a_shop_list_views import AdmiShopListView, AdmiShopCreateView, AdmiShopUpdateView

app_name = 'admi'
urlpatterns = [
    path('company/<int:pk>/', CompanyUpdateView.as_view(), name="company_update"),
    path('shop_list/', AdmiShopListView.as_view(), name="shop_list"),
    path('add_shop/', AdmiShopCreateView.as_view(), name="add_shop"),
    path('edit_shop/<int:pk>/', AdmiShopUpdateView.as_view(), name="edit_shop"),
]
