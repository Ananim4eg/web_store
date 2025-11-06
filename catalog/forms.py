from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(forms.ModelForm):
    """Форма для полей модели продуктов"""

    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image', 'category', 'price']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена должна быть положительным числом')
        return price

    def clean(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        cleaned_data = super().clean()
        product_name = cleaned_data.get('product_name')
        description = cleaned_data.get('description').split()

        if product_name and product_name.lower() in forbidden_words:
            self.add_error('product_name', 'Недопустимое название для продукта')

        if product_name and description:
            for word in description:
                if word.lower() in forbidden_words:
                    self.add_error('description', f'В описании присутствует недопустимое слово - {word}')
