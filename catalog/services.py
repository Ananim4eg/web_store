from catalog.models import Product, Category


class ProductService:

    @staticmethod
    def get_products_list_from_category(category_id):
        """Получает список всех продуктов в определенной категории"""

        products_list = Product.objects.filter(category_id=category_id).select_related('category').all()

        print(products_list)

        if not products_list.exists():
            return None
        return products_list

