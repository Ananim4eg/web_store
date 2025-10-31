from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactsView, ProductInfoDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home_list'),
    path('contacts/', ContactsView.as_view(), name='contacts_view'),
    path('product_info/<int:pk>/', ProductInfoDetailView.as_view(), name='product_detail')
]