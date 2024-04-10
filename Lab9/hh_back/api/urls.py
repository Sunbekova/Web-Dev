from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.get_all_companies, name='get_all_companies'),
    path('companies/<int:id>/', views.get_company_by_id, name='get_company_by_id'),
    path('companies/<int:id>/vacancies/', views.get_vacancies_by_company, name='get_vacancies_by_company'),
    path('vacancies/', views.get_all_vacancies, name='get_all_vacancies'),
    path('vacancies/<int:id>/', views.get_vacancy_by_id, name='get_vacanci_by_id'),
    path('vacancies/top_ten/', views.get_top_10_vacancies, name='get_top_10_vacancies'),
]