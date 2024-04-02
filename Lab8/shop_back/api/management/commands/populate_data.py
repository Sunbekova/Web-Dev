# shop_back/api/management/commands/populate_data.py

from django.core.management.base import BaseCommand
from api.models import Product, Category

class Command(BaseCommand):
    help = 'Populates initial data'

    def handle(self, *args, **kwargs):
        # Add your data population logic here
        # For example:
        category1 = Category.objects.create(name='Category 1')
        category2 = Category.objects.create(name='Category 2')

        Product.objects.create(name='Product 1', price=10.0, description='Description 1', count=5, is_active=True, category=category1)
        Product.objects.create(name='Product 2', price=15.0, description='Description 2', count=8, is_active=True, category=category2)
        # Add more products or categories as needed

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))
