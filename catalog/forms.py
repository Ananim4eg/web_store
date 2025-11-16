from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(forms.ModelForm):
    """Форма для полей модели продуктов"""
    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # получаем пользователя
        super().__init__(*args, **kwargs)
        self._restrict_fields()

        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-select'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

        if self.fields.get('publications_status'):

            self.fields['publications_status'].widget.attrs.update({
                'class': '.form-check'
            })

    def _restrict_fields(self):
        if not self.user:
            return
        if not self.user.has_perm('catalog.publications_status'):
            self.fields.pop('publications_status', None)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена должна быть положительным числом')
        return price

    def clean(self):
        cleaned_data = super().clean()
        product_name = cleaned_data.get('product_name')
        description = cleaned_data.get('description').split()

        if product_name and product_name.lower() in self.FORBIDDEN_WORDS:
            self.add_error('product_name', 'Недопустимое название для продукта')

        if product_name and description:
            for word in description:
                if word.lower() in self.FORBIDDEN_WORDS:
                    self.add_error('description', f'В описании присутствует недопустимое слово - {word}')

    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image', 'category', 'price', 'publications_status']
