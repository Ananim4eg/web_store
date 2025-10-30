from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products_info

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_info/<int:product_id>/', products_info, name='product_info')
]