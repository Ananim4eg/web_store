from django.shortcuts import render

def home(request):
    """Контроллер для рендеринга стартовой страницы"""
    return render(request, 'home.html')


def contacts(request):
    """Контроллер для рендеринга страницы контактов"""
    return render(request, 'contacts.html')
