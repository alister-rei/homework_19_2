from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    """Заполняет базу данных новыми данными и очищает ее от старых данных"""

    def handle(self, *args, **options):
        # Очистка базы данных от старых данных
        Product.objects.all().delete()

        category1 = Category.objects.get(id=1)
        category2 = Category.objects.get(id=2)
        category3 = Category.objects.get(id=3)
        category4 = Category.objects.get(id=4)

        # Заполнение базы данных новыми данными
        new_product = [
            {'name': 'Холодильник', 'description': 'Холодильник с морозильной камерой', 'category': category4, 'price': '54999.00'},
            {'name': 'Кабель USB type-C', 'category': category2, 'price': '150.00'},
        ]

        # for product in new_product:
        #     Product.objects.create(**data)

        product_for_create = []
        for product in new_product:
            product_for_create.append(
                Product(**product)
            )
        Product.objects.bulk_create(product_for_create)
