from django.http import JsonResponse
from .models import Product, Category

def get_all_products(request):
    products = Product.objects.all()
    data = [{'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description,
             'count': product.count, 'is_active': product.is_active, 'category': product.category.name} for product in products]
    return JsonResponse(data, safe=False)

def get_product(request, id):
    try:
        product = Product.objects.get(id=id)
        data = {'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description,
                'count': product.count, 'is_active': product.is_active, 'category': product.category.name}
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def get_all_categories(request):
    categories = Category.objects.all()
    data = [{'id': category.id, 'name': category.name} for category in categories]
    return JsonResponse(data, safe=False)

def get_category(request, id):
    try:
        category = Category.objects.get(id=id)
        data = {'id': category.id, 'name': category.name}
        return JsonResponse(data)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

def get_products_by_category(request, id):
    try:
        category = Category.objects.get(id=id)
        products = category.product_set.all()
        data = [{'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description,
                 'count': product.count, 'is_active': product.is_active, 'category': product.category.name} for product in products]
        return JsonResponse(data, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
