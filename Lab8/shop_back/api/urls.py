from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_all_products, name='get_all_products'),
    path('products/<int:id>/', views.get_product, name='get_product'),
    path('categories/', views.get_all_categories, name='get_all_categories'),
    path('categories/<int:id>/', views.get_category, name='get_category'),
    path('categories/<int:id>/products/', views.get_products_by_category, name='get_products_by_category'),
]
