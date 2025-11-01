from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, TemplateView, DetailView


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
