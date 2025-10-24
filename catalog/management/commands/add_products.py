from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
    """Добавляет продукты из фикстуры в базу данных"""

    help = 'Добавляет данные в базу данных'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'fixtures/product_fixture.json')

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены из фикстуры'))