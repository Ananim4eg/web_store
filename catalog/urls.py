from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactsView, ProductInfoDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductListView, ChoiceCategoryView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home_list'),
    path('contacts/', ContactsView.as_view(), name='contacts_view'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('product_info/<int:pk>/', ProductInfoDetailView.as_view(), name='product_detail'),
    path('choice_category/', ChoiceCategoryView.as_view(), name='choice_category'),
    path('product_list/<int:pk>/', ProductListView.as_view(), name='product_list'),
]