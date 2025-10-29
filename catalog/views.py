from django.shortcuts import render
from catalog.models import Product


def home(request):
    """Контроллер для рендеринга стартовой страницы"""
    return render(request, 'home.html')


def contacts(request):
    """Контроллер для рендеринга страницы контактов"""
    return render(request, 'contacts.html')


def product_info(request, product_id):
    """Контроллер для рендеринга страницы с информацией о товаре"""
    product = Product.objects.get(product_id)
    context = {
        'product': product
    }
    return render(request, 'product_info.html', context=context)