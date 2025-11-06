from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Product
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView


class HomeListView(ListView):
    """Контроллер для рендеринга стартовой страницы"""
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ContactsView(TemplateView):
    """Контроллер для рендеринга страницы контактов"""
    template_name = 'catalog/contacts.html'


class ProductInfoDetailView(DetailView):
    """Контроллер для рендеринга страницы с информацией о товаре"""
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    """Контроллер для страницы добавления продукта"""
    model = Product
    fields = ['product_name', 'description', 'image', 'category', 'price']
    template_name = 'catalog/create_product.html'
    success_url = reverse_lazy('catalog:home_list')


class ProductUpdateView(UpdateView):
    """Контроллер для страницы изменения продукта"""
    model = Product
    fields = ['product_name', 'description', 'image', 'category', 'price']
    template_name = 'catalog/update_product.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    """Контроллер для страницы подтверждения удаления продукта"""
    model = Product
    template_name = 'catalog/delete_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:home_list')
