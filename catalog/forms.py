from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(forms.ModelForm):
    """Форма для полей модели продуктов"""
    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']

    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

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
