from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from catalog.forms import ProductForm
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


class ProductInfoDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для рендеринга страницы с информацией о товаре"""
    model = Product
    template_name = 'catalog/product_info.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        """Добавляем флаг с определенным правом и передаем в форму"""
        context = super().get_context_data(**kwargs)
        context['is_moderator'] = self.request.user.groups.filter(name='Модератор продуктов').exists()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для страницы добавления продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_product.html'
    success_url = reverse_lazy('catalog:home_list')

    def form_valid(self, form):
        """Добавляем текущего авторизованного пользователя как владельца при создании продукта"""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для страницы изменения продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/update_product.html'
    context_object_name = 'product'


    def get_form(self, form_class=None):
        """Формируем поля формы в зависимости от прав пользователя"""
        form = super().get_form(form_class)

        if not self.request.user.has_perm('catalog.publications_status'):
            form.fields.pop('publications_status', None)

        return form

    def get_form_kwargs(self):
        """Передаем текущего пользователя в форму"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        """Добавляем флаг с определенным правом и передаем в форму"""
        context = super().get_context_data(**kwargs)
        context['publications_status'] = self.request.user.has_perm('catalog.publications_status')
        return context

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для страницы подтверждения удаления продукта"""
    model = Product
    template_name = 'catalog/delete_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:home_list')
    permission_required = 'catalog.Can_delete_продукт'

    def handle_no_permission(self):
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied("У вас нет прав на удаление этого объекта.")


class Error403View(TemplateView):
    """Контроллер для страницы с ошибкой доступа"""
    template_name = 'catalog/403.html'
